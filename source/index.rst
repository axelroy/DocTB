.. AutoML's documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AutoML's documentation!
=============================================

Abstract
============

.. raw:: latex

   \clearpage

.. toctree::
   :maxdepth: 4
   :numbered:
   :caption: Contents:

.. raw:: latex

   \clearpage


Introduction
============

Le présent document fait office de rapport de projet.
Il permet de comprendre le contexte de celui-ci, de reconstituer son cheminement du projet,
de comprendre les choix et les déductions effectuées, ainsi que de connaître l'état final
du travail et les perspectives d'amélioration.

Contexte du projet
------------


Le présent projet s'inscrit dans le cadre du travail de Bachelor en Informatique option "Développement logiciel
et multimédia", réalisé à la HE-ARC de Neuchâtel.

Le projet est effectué pour le CHUV-LREN dans le cadre du projet Human Brain Project.

Human Brain projet
~~~~~~~~~~~~

Ce projet s’inscrit dans le cadre du projet Européen « Human Brain Project ».
Ce chapitre vise à expliquer le contexte de la partie du projet qui nous intéresse.

Cadre du sous-projet 8 (SP8)
~~~~~~~~~~~~

Présentation de la plateforme MIP
____________

Le but du sous-projet 8 du HBP est de fournir une plateforme pour effectuer des
expériences neuroscientifiques sur des données de patients recueillies à travers les
cliniques et hôpitaux partenaires. Etant donné la nature médicale de ces données,
elles sont bien évidemment anonymisées, et il n’est pas possible de retrouver les
données d’un patient, car les données sont présentées sous la forme d’agrégation
par caractéristique, comme le présente la capture d’écran suivante :

.. figure:: images/Agregation_features_MIP.png
   :width: 350px
   :align: center
   :alt: Représentation des caractéristiques d'intérêts

   Représentation des caractéristiques d'intérêts.

En selectionnant un des ronds blancs, on accède à la variable en question,
et on peut observer différentes statistiques, comme par exemple des vues sous forme d’histogrammes.

.. figure:: images/Histogram_features_MIP.png
   :width: 400px
   :align: center
   :alt: Exemple d'histogramme d'une variable.

   Exemple d'histogramme d'une variable.

Il est ainsi possible d’accéder à toutes les caractéristique médicales et ainsi
de les analyser manuellement. La plateforme permet aussi de formuler des expériences
basées sur les données, afin de proposer un modèle personnalisé qui permet d’essayer
de trouver des liens entre les variables des patients et leur diagnostiques médicaux.
La plateforme permet vise à formuler des expériences liées à Alzheimer,
mais d’autres maladie neurologiques pourraient être visées. A partir d’une caractéristique,
l’utilisateur peut décider de formuler une expérience en choisissant dans laquelle
des catégories suivantes il compte l’impliquer :

* Variable
* Co-variable
* Filtre

Via l’interface suivante :

.. figure:: images/Variables_experiences.png
   :width: 450px
   :align: center
   :alt: Exemple de formulation d'expérience, étape selection des variables. Cet exemple vise à trouver un lien entre la quantité de matière grise dans le Cuneus en fonction de l'age et du sexe.

   Exemple de formulation d'expérience, étape selection des variables. Cet exemple vise à trouver un lien entre la quantité de matière grise dans le Cuneus en fonction de l'age et du sexe.

Ce qui nous amène vers la possibilité d’analyser des graphes mêlant les différentes
variables. Il est encore possible de paramétrer la représentation sur l’axe via
une boite à outils, afin de faire ressortir les informations intéressantes.

La partie intéressante dans le cadre de ce projet est la possibilité, à partir des
variables sélectionnées, de lancer une expérience d’apprentissage automatique
(machine learning) afin de trouver le modèle qui permet de représenter au mieux
le lien entre les caractéristiques et le diagnostique.

L’aide pour la configuration de l’expérience est présentée ainsi :

.. figure:: images/Resultat_nonML_experiment.png
   :width: 400px
   :align: center
   :alt: Résultat de l'expérience de l'illustration 3.  Représentation de la quantité de matière grise en cm3 en fonction de l'age et du sexe (bordeau = femme, rose = homme).

   Résultat de l'expérience de l'illustration 3.  Représentation de la quantité de matière grise en cm3 en fonction de l'age et du sexe (bordeau = femme, rose = homme).

Les étapes 1 et 2 sont celles qui nous intéressent :

L’étape 1 correspond à la sélection d’un algorithme de machine learning dans
la liste fournie (catégories : analyse statistique, extraction de caractéristiques
et modèle prédictif). Le modèle choisi influence fortement les résultats de l’expérience.

Lorsque le modèle est sélectionne, il est possible, suivant le modèle, de devoir
renseigner des « *paramètres* » pour celui-ci. Nous appellerons ces paramètres
des « *hyper-paramètres* », afin d’éviter la confusion avec les paramètres
qui sont les coefficients internes qui ont été déterminés après l’entraînement.
Les hyper-paramètres définissent un fonctionnement interne (par exemple, pour le
modèle KNN1, l’hyper-paramètre k désigne le nombre des voisins les plus proches
sur lesquels on veut travailler). Le choix de ces hyper-paramètres est donné au
points deux de cette marche à suivre. Pour un même modèle, le choix d’un
hyper-paramètres plutôt qu’un autre change à nouveau drastiquement les résultats.

Il peut paramétrer plusieurs configurations modèle-paramètres pour une expérience.
Une expérience ne donne pas instantanément de résultats. L’utilisateur est notifié
lorsque les résultats sont consultables.

C’est ici que s’inscrit le projet. L’utilisateur, qui est probablement plus un spécialiste
en neuroscience qu’en informatique, se trouve à paramétrer et choisir des données
qui sont liées uniquement à l’informatique.

But du projet
_____________

Ce projet a pour but de mettre en place un moyen pour que l’utilisateur n’ait plus
à s’occuper du choix du modèle et du paramétrage pour son expérience, et que la
plateforme s’occupe de trouver automatiquement la meilleure configuration possible.
Dans l’idéal, l’utilisateur n’a qu’un bouton a presser pour cette étape.


Cahier des charges (lien vers les annexes je suppose, en sachant qu'il est expliqué en détail dans le document)
============

Se référer au cahier des charges fourni en annexes.



Etat de l'Art : Passage en revue des différentes technologies, de la plus globale à la plus précise. En vue : Machine learning, Docker, Scala, AKKA, Marathon, even. ZeroMQ + autres technologies qui pourraient surgir.
============

Avant de se lancer dans la partie plus en détail dans la description de la plateforme,
il est intéressant d’effectuer un état de l’art des technologies qui pourraient
nous intéresser. Etant donné que le projet consiste à ajouter des fonctionnalités
à un projet existant, cette section décrira les technologies actuellement existantes,
ainsi que les technologies qui seront probablement utilisées, ou tout du moins
leur champ d’application.

Cette section est rédigée en listant les différentes technologies, de la plus globale
à la plus précise en terme d’utilisation dans le projet.

Théorie ML
------------

Le machine learning (apprentissage automatique en francais), est un champ d’activité
de l’intelligence artificielle qui vise à permettre à une machine d’apprendre par elle-même
plutôt que d’en fixer tous les comportements de manière programmatique.
Elle est particulièrement utilisée dans les problématiques où le nombre de cas
est trop important pour être codés à la mano. Le panel d’utilisation est large,
il peut par exemple concerner :


* L’analyse de graphes ou de données
* La classification d’individus
* La résolution de problèmes de régression
* La reconnaissance d’objets
* L’analyse de documents (notamment pour les moteurs de recherche)
* La reconnaissance de caractères manuscrits
* L’aide au diagnostiques médicaux

Dans notre cas, l’apprentissage automatique est implémenté dans la plateforme via les méthodes suivantes :

* TODO : Remplir via la Query-list

Mais on peut aussi ajouter à la plateforme d’autres méthodes d’apprentissage automatique
via des containers Docker. TODO : Compléter cette fonctionnalité quand on aura plus d’infos.

Apprentissage supervisé
~~~~~~~~~~~~

Dans cette méthodologie, on connait déjà les classes que l’on souhaite pouvoir déterminer
automatiquement via l’algorithme. Ces classes sont tirées des données par un expert.
Dans certains cas, il est aussi possible d’attribuer une probabilité d’appartenance à une classe.
L’apprentissage se déroule généralement en deux phases. La première phase est dite d’entrainement.
Elle consiste à déterminer un modèle qui permet de reproduire pour de nouvelles données la même
classification/régression que celle donnée via les labels. La seconde phase est dite de validation.
Elle consiste à déterminer si le modèle entrainé est pertinent, via des méthodes métriques.
Ces deux phases ne s’effectuent pas sur les mêmes données. La phase d’entrainement nécessite
une quantité d’informations suffisantes afin d’avoir un modèle représentatif.

Apprentissage non supervisé
~~~~~~~~~~~~

Cet apprentissage s’applique à des données qui ne sont pas labellées par des classes.
C’est ici à la machine de déterminer les différentes classes qui représentent le problème.
A partir d’un ensemble de données en entrées, il va chercher à créer des classes représentatives
pour celles-ci, en maximisant la distance inter-classe, et en minimisant la distance des éléments intra-classe.

.. figure:: images/distance_illustration.png
   :width: 300px
   :align: center
   :alt: Représentation des distances inter-classe et intra-classe. Illustration issue du site MSDN TODO:LINK

   Représentation des distances inter-classe et intra-classe. Illustration issue du site MSDN

Cette méthodologie peut aussi permettre d’analyser la relation entre les variables, par
exemple pour réduire la dimension des vecteurs d’entrées.

Apprentissage semi-supervisé
~~~~~~~~~~~~

Etant donné que l’apprentissage supervisé nécessite un labelisation des données par expert,
il devient très coûteux de réaliser ce travail au fur et à mesure que les données augmentent.
L’utilisation de données labellées, liées à des données labellées, peut permettre d’améliorer
la qualité de l’apprentissage. Par exemple, il est ainsi possible d’utiliser un classificateur
crée par l’apprentissage supervisé, et un autre crée par l’apprentissage non-supervisé.

Idéalement, les deux classificateurs ne se basent pas sur les mêmes caractéristiques, ce qui
permet de recouper les deux classificateurs afin d’affiner la classification finale.

Optimisation automatique du pipeline d'apprentissage
------------

De manière générale, le Machine Learning est décrit comme une suite d'opérations à
effectuer de manière linéaire pour permettre de résoudre une problématique. On parle dès
lors de pipeline, étant donné que chaque étape est effectuée à la manière d'un flux
d'opérations, de la première à la dernière.

Ce pipeline est généralement découpé en deux phases distinctes :

* Extraction, normalisation et éventuellement construction des caractéristiques à partir des données brutes.
* Application d'un modèle statistique ou linéaire pour effectuer, selon la problématique, une classification ou une régression.

On peut représenter ce flux via la représentation suivante :

.. figure:: images/ml_pipeline.png
   :width: 500px
   :align: center
   :alt: Exemple d'un pipeline de Machine Learning, tiré de la documentation TPOT TODO:LINK et modifié pour supprimer les parties liées à TPOT.

   Exemple d'un pipeline de Machine Learning, tiré de la documentation TPOT TODO:LINK et adapté.

Dans une approche traditionnelle d'optimisation d'une expérience de Machine Learning,
on essaie de faire varier les hyper-paramètres du modèle (p.e via les grid-search TODO:Link vers la doc http://scikit-learn.org/stable/modules/grid_search.html).

Cette méthode permet d'optimiser les hyperparamètres du modèle, mais celui-ci doit avoir
été selectionné manuellement auparavant.

Le machine le




Technologies
------------

Analyse
============

La place de Woken dans l'architecture globale (succinct, sans parler de toute la plateforme)
------------

Fonctionnement interne de Woken
------------

But
~~~~~~~~~~~~

Entrées et sorties
~~~~~~~~~~~~

Flux de traitement (présentation du diagramme d'acteurs réalisé en début de projet)
~~~~~~~~~~~~

Conception (A voir si on précise la conception avant)
============

Modification du workflow Woken
------------

Nouveau diagramme d'acteurs imaginé, et comment on coupe le workflow actuel
~~~~~~~~~~~~

La problématique Marathon (intégration encore non définie)
~~~~~~~~~~~~


Implémentation réalisée
============

Création d'un container interactif
------------

Problème initial
~~~~~~~~~~~~

Présentation des solutions au problème
~~~~~~~~~~~~

Choix effectué
~~~~~~~~~~~~

Modification du workflow Woken
------------

Ajout du nouveau container dans la configuration
~~~~~~~~~~~~

Intégration de TPOT
------------

A déterminer, mais je suppose : Les contraintes posées par la bibliothèque, les choix qui ont du être effectués.
~~~~~~~~~~~~

Eventuellement, si plus de travail a été effectué, présentation de celui-ci.
------------


Validation (Expérience)
============

6.1 Présentation de l'expérience
    6.1.1 pourquoi
    6.1.2 comment
    6.1.3 les conditions de tests
6.2 Résultats de l'expérience
6.3 Discussion des résultats


Conclusion
============

Etat des lieux au moment du rendu
------------

- Atteintes des objectifs

  - Le contexte du mandant a-t-il été compris?
  - L'API se superposant à Marathon fonctionne-t-elle?
  - Un format de métadonnées a-t-il été spécifié? Existe-t-il un moyen
    de vérifier que telle ou telle image Docker respecte ce format?
  - Un démonstrateur a-t-il été développé?

- Améliorations possibles

.. Le développeur a pris un risque en prenant en tester des technologies
.. qu'il n'utiliserait peut-être même pas mais cela lui a permis de mieux saisir
.. la problématique.

Perspectives et améliorations
------------

Bilan personnel (Présenter ce qui apporte quelque chose)
------------

Remerciements
=============

Annexes, références et Table des illustrations.
============

.. .. raw:: latex

..  \bibliographystyle{plain}
..  \bibliography{references.bib}

.. bibliography:: references.bib
   :notcited:
   :style: unsrt

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
