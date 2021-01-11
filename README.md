# YearPredictionMSD Data Set 
https://archive.ics.uci.edu/ml/datasets/YearPredictionMSD

## Python for data analysis

* Diane DU PELOUX
* Mohammad Reza ZOHRABI

## Objectif du projet

Pour notre étude, nous avons pour sujet le dataset “Million Song”. Nous pourrons décrire ce jeu de données par la citation officielle suivante :
“Le dataset Million Song est une collection gratuite de fonctionnalités audio et de métadonnées pour un million de morceaux de musique populaire contemporaine.
Le cœur de l’ensemble de données est l’analyse des caractéristiques et les métadonnées d’un million de chansons, fournies par The Echo Nest. L’ensemble de données n’inclut pas d’audio, seulement les fonctionnalités dérivées.

Pour en connaître plus sur notre dataset nous nous poserons les questions suivantes et y répondons par différents moyens de visualisation :
  Quelle est la répartition du nombre de musiques par année (à quelle point notre base de données sera efficiente pour nos futurs modèles?) ?
  Comment sont répartis les différents timbres moyens ? A quoi correspondent-ils?
  Comment est réparti un timbre moyen sur plusieurs années (100 ans) ?
  Quelle est la corrélation entre chaque timbre moyen ?
  Estimation de la corrélation entre timbre et décennie qui nous permettra de nous diriger vers notre problémtique finale : Réussir à définir l'année (décennie) de sortie d'une     chanson en fonction des timbres dont elle est constituée.

## Description du dataset

Dans notre dataset nous pouvons retrouver par champs  :

  [valeur 1] L’année cible allant de 1922 à 2011
  [valeur 2 à 14] TimbreAverage(1 à 12)
  [valeur 15 à 91] TimbreCovariance(1 à 78)

Ces fonctionnalités ont été extraites des fonctionnalités 'timbre' de l’API Echo Nest. Les auteurs ont pris la moyenne et la covariance sur tous les «segments» et chaque segment a été décrit par un vecteur de timbre à 12 dimensions. Le timbre des signaux audio n’a pas été clairement défini mathématiquement. On a émis l’hypothèse que la structure temps-fréquence des signaux audio contribue à la propriété du timbre. Dans certains articles, la matrice de covariance à partir des signaux de sortie de banque de filtres multi-bandes d’un signal audio  est réalisée et le filtre Common Spatial Pattern (CSP) est appliqué pour caractériser le timbre des signaux audio. Les résultats des simulations confirment que la matrice de covariance des signaux audio multibandes et du filtre CSP peut être utilisée comme caractéristique potentielle de la classification des timbres.
