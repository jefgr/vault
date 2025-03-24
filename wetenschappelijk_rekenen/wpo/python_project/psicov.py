import csv
import numpy as np


### PUBLIC ###

def retrieve_covariance_matrix(filename):
    """
    Retrieve a covariance matrix stored in the given file.
    """
    return np.asmatrix(csv2matrix(filename, ','))

def retrieve_predicted_contacts(M_inv):
    """
    Retrieve the predicted contacts from the inverse covariance matrix M_inv.
    """
    return list(zip(*compute_scores(M_inv)))[0]

def retrieve_true_contacts(filename, thresh):
    """
    Retrieve amino-pair contacts from the given file.
    A contact is considered a pair within a distance of ‘thresh’ from each other.
    """
    return list(map(lambda x: (int(x[0]), int(x[1])), filter(lambda x: x[2] <= thresh, csv2matrix(filename))))

def fraction_of_correct_predictions(pred_contacts, true_contacts):
    """
    Compute the fraction of correctly predicted contacts w.r.t. the true contacts.
    """
    predictions = list(map(lambda x: x in true_contacts, pred_contacts))
    return sum(predictions) / len(predictions)



### PRIVATE ###

def csv2matrix(filename, delim=' '):
    """
    Read a csv file and convert it into a matrix.
    """
    with open(filename, 'r') as f:
        csvreader = csv.reader(f, delimiter=delim)
        M = [list(map(float, row)) for row in csvreader]
    return M

def compute_scores(M):
    """
    Compute the PSICOV scores from the amino-amino correlation matrix M.
    """
    n = int(len(M) / 21)
    contacts = np.zeros((n,n))
    scores = {}

    for i in range(n):
        for j in range(i+1, n):
            #print(M[(21*i):(21*(i+1)-1),(21*j):(21*(j+1)-1)])
            contacts[i, j] = np.sum(np.abs(M[(21*i):(21*(i+1)-1),(21*j):(21*(j+1)-1)]))
            contacts[j, i] = contacts[i, j]

    sum_contacts_i = list(map(sum, contacts))
    sum_contacts = sum(sum_contacts_i)

    for i in range(n):
        for j in range(i+1, n):
            if contacts[i, j] > 0.0:
                score = contacts[i, j] - (sum_contacts_i[i]*sum_contacts_i[j]/sum_contacts)
                scores[(i, j) if i < j else (j, i)] = score
    scores = list(scores.items())
    scores.sort(key=lambda x: x[1], reverse=True)
    
    return scores

def write_covariance_matrix(M, filename):
    """
    Write a covariance matrix to a cvs file.
    """
    with open(filename, 'w') as f:
        csvwriter = csv.writer(f, delimiter=',')
        for i in range(len(M)):
            csvwriter.writerow(np.ravel(M[i,:]))