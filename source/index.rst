.. AutoML's documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AutoML's documentation!
=============================================

.. raw:: latex

   \clearpage

.. toctree::
   :numbered:
   :maxdepth: 5

.. raw:: latex

   \clearpage

Introduction
============

Le présent document fait office de rapport de projet.
Il permet de comprendre le contexte de celui-ci, de reconstituer son cheminement du projet,
de comprendre les choix et les déductions effectuées, ainsi que de connaître l'état final
du travail et les perspectives d'amélioration.

Contexte du projet
----------------

Le présent projet s'inscrit dans le cadre du travail de Bachelor en Informatique option "Développement logiciel
et multimédia", réalisé à la HE-ARC de Neuchâtel.

Le projet est effectué pour le CHUV-LREN dans le cadre du projet Human Brain Project.

Human Brain projet
~~~~~~~~~~~~

Ce projet s’inscrit dans le cadre du projet Européen « Human Brain Project ».
Ce chapitre vise à expliquer le contexte de la partie du projet qui nous intéresse.


Présentation de la plateforme MIP
~~~~~~~~~~~~~~

Le but du sous-projet 8 du HBP est de fournir une plateforme pour effectuer des
expériences neuroscientifiques sur des données de patients recueillies à travers les
cliniques et hôpitaux partenaires. Etant donné la nature médicale de ces données,
elles sont bien évidemment anonymisées, et il n’est pas possible de retrouver les
données d’un patient, car les données sont présentées sous la forme d’agrégation
par caractéristique, comme le présente la :num:`figure #features`

.. raw:: latex

   \clearpage

.. _features:
.. figure:: images/Agregation_features_MIP.png
   :width: 500px
   :align: center
   :alt: Représentation des caractéristiques d'intérêts

   *Représentation des caractéristiques d'intérêts.*

En sélectionnant un des ronds blancs, on accède à la variable en question,
et on peut observer différentes statistiques, comme par exemple des vues sous forme d’histogrammes [cf :num:`figure #histogram`]

.. raw:: latex

   \clearpage


.. _histogram:
.. figure:: images/Histogram_features_MIP.png
   :width: 450px
   :align: center
   :alt: Exemple d'histogramme d'une variable.

   *Exemple d'histogramme d'une variable.*

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

Via l’interface suivante présentée en :num:`figure #variables`.

.. _variables:
.. figure:: images/Variables_experiences.png
   :width: 450px
   :align: center
   :alt: Exemple de formulation d'expérience, étape selection des variables. Cet exemple vise à trouver un lien entre la quantité de matière grise dans le Cuneus en fonction de l'age et du sexe.

   *Exemple de formulation d'expérience, étape selection des variables. Cet exemple vise à trouver un lien entre la quantité de matière grise dans le Cuneus en fonction de l'age et du sexe.*

Ce qui nous amène vers la possibilité d’analyser des graphes mêlant les différentes
variables. Il est encore possible de paramétrer la représentation sur l’axe via
une boite à outils, afin de faire ressortir les informations intéressantes, comme présenté à la :num:`figure #resultnoml`

.. _resultnoml:
.. figure:: images/Resultat_nonML_experiment.png
   :width: 500px
   :align: center
   :alt: Résultat de l'expérience formulée à la :num:`figure #variables`. Représentation de la quantité de matière grise en cm3 en fonction de l'age et du sexe (bordeau = femme, rose = homme).

   *Résultat de l'expérience formulée à la :num:`figure #variables`. Représentation de la quantité de matière grise en cm3 en fonction de l'age et du sexe (bordeau = femme, rose = homme).*

La partie intéressante dans le cadre de ce projet est la possibilité, à partir des
variables sélectionnées, de lancer une expérience d’apprentissage automatique
(Machine Learning) afin de trouver le modèle qui permet de représenter au mieux
le lien entre les caractéristiques et le diagnostique.

L’aide pour la configuration de l’expérience est présentée comme en :num:`figure #helpconfig`

.. _helpconfig:
.. figure:: images/description_experience.png
   :width: 600px
   :align: center
   :alt: Aide pour la formulation d'une expérience de Machine Learning.

   *Aide pour la formulation d'une expérience de Machine Learning.*

Les étapes 1 et 2 sont celles qui nous intéressent :

L’étape 1 correspond à la sélection d’un algorithme de *Machine Learning* dans
la liste fournie (catégories : analyse statistique, extraction de caractéristiques
et modèle prédictif). Le modèle choisi influence fortement les résultats de l’expérience.

Lorsque le modèle est sélectionne, il est possible, suivant le modèle, de devoir
renseigner des « **paramètres** » pour celui-ci. Nous appellerons ces paramètres
des « **hyper-paramètres** », afin d’éviter la confusion avec les paramètres
qui sont les coefficients internes qui ont été déterminés après l’entraînement.
Les hyper-paramètres définissent un fonctionnement interne (par exemple, pour le
modèle KNN, l’hyper-paramètre k désigne le nombre des voisins les plus proches
sur lesquels on veut travailler). Le choix de ces hyper-paramètres est donné au
points deux de cette marche à suivre. Pour un même modèle, le choix d’un
hyper-paramètres plutôt qu’un autre change à nouveau drastiquement les résultats.

Il peut définir plusieurs configurations "modèle-paramètres" pour une expérience.
Une expérience ne donne pas instantanément ses résultats. L’utilisateur est notifié
lorsque les résultats sont consultables.

C’est ici que s’inscrit le projet. L’utilisateur, qui est probablement plus un spécialiste
en neuroscience qu’en informatique, se trouve obligé de paramétrer et choisir des données
qui sont liées uniquement à l’informatique.

But du projet
~~~~~~~~~~~~~~

Ce projet a pour but de mettre en place un moyen pour que l’utilisateur n’ait plus
à s’occuper du choix du modèle et du paramétrage pour son expérience, et que la
plateforme s’occupe de trouver automatiquement la meilleure configuration possible.
Dans l’idéal, l’utilisateur n’a qu’un bouton a presser pour cette étape.


Cahier des charges (lien vers les annexes je suppose, en sachant qu'il est expliqué en détail dans le document)
============

Se référer au cahier des charges fourni en annexes.

Etat de l'Art
============

Avant de se lancer dans la partie plus en détail dans la description de la plateforme,
il est intéressant d’effectuer un état de l’art des technologies qui pourraient
nous intéresser. Etant donné que le projet consiste à ajouter des fonctionnalités
à un projet existant, cette section décrira les technologies actuellement existantes,
ainsi que les technologies ajoutées, ou tout du moins leur champ d’application.

Cette section est rédigée en listant les différentes technologies, de la plus globale
à la plus précise en terme d’utilisation dans le projet.

Théorie Machine Learning
------------

Le *Machine Learning* (apprentissage automatique en francais), est un champ d’activité
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

* Résumé statistique ;
* Analyse de la variance (anova) ;
* Régression linéaire ;
* KNN
* Classification naïve bayésienne

Mais on peut aussi ajouter à la plateforme d’autres méthodes d’apprentissage automatique
via des containers Docker vierges qui sont fournis par le projet.

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
pour celles-ci, en maximisant la distance inter-classe, et en minimisant la distance des éléments intra-classe
comme représenté sur la :num:`figure #distanceml`.:num:`figure #distanceml`

.. _distanceml:
.. figure:: images/distance_illustration.png
   :width: 300px
   :align: center
   :alt: Représentation des distances inter-classe et intra-classe. Illustration issue du site Microsoft :cite:`@theoryMLMS`

   Représentation des distances inter-classe et intra-classe. Illustration issue du site MSDN :cite:`@theoryMLMS`

Cette méthodologie peut aussi permettre d’analyser la relation entre les variables, par
exemple pour réduire la dimension des vecteurs d’entrées.

Apprentissage semi-supervisé
~~~~~~~~~~~~~~~

Etant donné que l’apprentissage supervisé nécessite un labelisation des données par expert,
il devient très coûteux de réaliser ce travail au fur et à mesure que les données augmentent.
L’utilisation de données labellées, liées à des données labellées, peut permettre d’améliorer
la qualité de l’apprentissage. Par exemple, il est ainsi possible d’utiliser un classificateur
crée par l’apprentissage supervisé, et un autre crée par l’apprentissage non-supervisé.

Idéalement, les deux classificateurs ne se basent pas sur les mêmes caractéristiques, ce qui
permet de recouper les deux classificateurs afin d’affiner la classification finale.

Optimisation automatique du pipeline d'apprentissage
---------------

De manière générale, le *Machine Learning* est décrit comme une suite d'opérations à
effectuer de manière séquentielle pour permettre de résoudre une problématique. On parle dès
lors de pipeline, étant donné que chaque étape est effectuée, à la manière d'un flux
d'opérations, de la première à la dernière.

Ce pipeline est généralement découpé en deux phases distinctes :

* Extraction, normalisation et éventuellement construction des caractéristiques à partir des données brutes.
* Application d'un modèle statistique ou linéaire pour effectuer, selon la problématique, une classification ou une régression.

On peut représenter ce flux via la :num:`figure #mlpipeline`:

.. _mlpipeline:
.. figure:: images/ml_pipeline.png
   :width: 650px
   :align: center
   :alt: Exemple d'un pipeline de *Machine Learning*, tiré de la documentation TPOT :cite:`Olson2016EvoBio` et modifié pour supprimer les parties liées à TPOT.

   Exemple d'un pipeline de Machine Learning, tiré de la documentation TPOT :cite:`Olson2016EvoBio` et adapté pour supprimer les parties liées à TPOT.

.. _mlphases:
On peut en décrire les phases ainsi :

* **Data Cleaning** : Mise en forme des données et nettoyage. Ceci peut consister à renseigner les données manquantes.
* **Features Preprocessing** : Transformation des caractéristiques pour les rendre plus utilisables dans le contexte, par exemple en les normalisant.
* **Features Selection** : Sélection des caractéristiques les plus pertinentes pour le modèle.
* **Feature Construction** : Création de nouvelles caractéristiques à partir des données.
* **Model Selection** : Sélection du type de modèle ainsi que les hyper-paramètres liés à celui-ci (p.e. pour un réseau de neurones, le nombre de couches de neurones). Actuellement, l’utilisateur doit les configurer lui-même, et même un utilisateur expert ne peut pas garantir que ce sont les meilleurs hyper-paramètres possibles.
* **Parameter Optimization** : le choix d’un modèle détermine les paramètres qui lui sont liés (p.e. pour un réseau de neurones, le poids de chaque neurone). Ces paramètres  influencent énormément la performance du modèle. Ils sont optimisés lors de cette phase.
* **Model Validation** : En sortie, nous avons, pour un ensemble de caractéristiques donnée, un modèle et le hyper-paramètres de ce modèle. Il faut ensuite valider ce modèle sur un ensemble de sujets différents afin de déterminer sa pertinence.

Dans une approche traditionnelle d'optimisation d'une expérience de *Machine Learning*,
on essaie de faire varier les hyper-paramètres du modèle (p.e via les grid-search :cite:`@datagridsearchdoc` de Scikit-Learn :cite:`scikit-learn`).

Cette méthode permet d'optimiser les hyper-paramètres du modèle. Ce dernier doit avoir
été sélectionné manuellement auparavant par l'utilisateur. De plus, l'étendue et le pas des hyper-paramètres sont
eux-aussi déterminés manuellement. Cela réduit le domaine d'exploration.

Une tendance émergente de ces dernières années est d'utiliser des méthodes d'intelligence artificielle pour
explorer l'espace des solutions de manière automatique et optimisée. Cette exploration est souvent effectuée
via des algorithmes génétiques [TODO:Lien(s) qui explique les principes] car ils
correspondent à la problématique d'exploration d'un espace de solutions de grande dimension.
Cette exploration est effectuée de manière non dirigée tout en fournissant un résultat exploitable.

Les réelles avancées dans le domaine sont récentes, les premiers articles concrets datent de
2016, et il est difficile de trouver des exemples dans un domaine concret, prouvant l'efficacité de *l'Automated Machine Learning* .
Les créateurs de bibliothèque TPOT :cite:`Olson2016EvoBio` ont rédigé deux papiers :cite:`olson2016evaluation` :cite:`olson2016tpot`
d'exemple d'applications dans des cas réels, sur la classification de cas de cancers de la prostate,
de manière conventionnelle, et via l'approche *Automed Machine Learning*, et ont pu mettre en avant
une amélioration des résultats.
Google a récemment communiqué son intérêt pour le domaine, en annoncant l'ouverture d'un département
sur la recherche de cette discipline :cite:`@googleautoml`. Certains sites spécialisés :cite:`@stateautoml` :cite:`@hhusain`
décrivent ce domaine avec intérêt, mais en précisant que les résultats ne sont pas encore
probants, et que, pour le moment, elle n'est pas applicable à toutes les problématiques.

Dans le cadre du projet, étant donné que les utilisateurs ne sont pas experts dans
le domaine du *Machine Learning*, il est que les résultats soient meilleurs que
les configurations des utilisateurs.

Si le travail abouti à une expérience, il est possible que celui-ci soit publié.

Technologies
---------------

TPOT
~~~~~~~~~~~~~~~

*TPOT* :cite:`Olson2016EvoBio` est une bibliothèque *open-source* permettant l'optimisation
de pipeline automatisée, alias *automated Machine Learning*. Elle se distingue des autres
bibliothèques telles que Auto-WEKA :cite:`@autoweka` et Hyperopt :cite:`@hyperopt` par le fait
qu'il est capable non seulement de faire varier les modèles et le hyper-paramètres,
mais qu'elle est aussi capable de sélectionner, construire ou d'effectuer du préprocessing
sur les caractéristiques. *TPOT* dispose d'une communauté active, et le créateur *Randy Olson*
répond très rapidement aux issues postées sur le *Github* de *TPOT*.

Celà se représente comme sur la figure :num:`figure #mlpipelinetpot`.

.. _mlpipelinetpot:
.. figure:: images/tpot-ml-pipeline.png
   :width: 650px
   :align: center
   :alt: Exemple d'un pipeline de Machine Learning, avec les parties gérées automatiquement par TPOT. Illustration tirée de la documentation TPOT :cite:`Olson2016EvoBio`

   Exemple d'un pipeline de Machine Learning, avec les parties gérées automatiquement par TPOT. Illustration tirée de la documentation TPOT :cite:`Olson2016EvoBio`


Les différentes étapes ont la même signification que présenté au point de :ref:`présentation des phases typiques de machine learning <mlphases>`,
au dessous de la :num:`figure #mlpipeline`.

Cette bibliothèque est codée en Python, et se base sur les modèles de Scikit-learn :cite:`scikit-learn`, ce qui
permet d'avoir des résultats exploitables directement via cette bibliothèque *Python*. Pour son implémentation,
elle se base sur une représentation du pipeline sous forme d'arbre pour les pipeline (qui correspondent aux chromosomes
dans la théorie de *Darwin*), et effectuer des mutations en croisant des parties de cet arbre,
en en coupant des branches, ou en créant de nouvelles.


Systèmes distribués
~~~~~~~~~~~~~~~

Historiquement, avant que le web ne vienne changer la donne, une application était
localisé sur une machine unique, et son architecture se présentait comme sur la :num:`figure #computerarchi`

.. raw:: latex

   \clearpage

.. _computerarchi:
.. figure:: images/computer_architecture.png
   :width: 200px
   :align: center
   :alt: Architecture simple basée sur une application unique

   Architecture simple basée sur une application unique : crédits @ Groovytron :cite:`@groovytron`

Avec l'augmentation de la demande, la première approche pour augmenter la capacité
de réponse a été de parraléliser plusieurs machines sur le réseau, et d'effectuer
un balancage de charge entre les différentes instances, en fonction des moyens.

Les machines sont déployées en cluster (groupes de machines), et le *load-balancer*
s'occupe de répartir les requêtes, comme présenté à la :num:`figure #highavailability`.

.. _highavailability:
.. figure:: images/high_availability_architecture.png
   :width: 500px
   :align: center
   :alt: Architecture orientée haute disponibilité et «scalabilité»

   *Architecture orientée haute disponibilité et «scalabilité» : crédits @ Groovytron*

Avec la venue d'internet, l'utilisation des applications a changée, et elles ont
été amenées à communiquer entre elles, afin de partager des données ou des services.

Dès lors, le découpage des applications s'est effectué par bloc, chaque application
étant indépendante, mais fourni une interface comme point d'entrée pour communiquer,
et s'appuie généralement sur un format d'encodage haut-niveau (XML, JSON, ...).
pour formuler des réponses aux autres applications. On a ainsi un découpage plus fin
des fonctionnalités, mais ce découpage engendre un travail supplémentaire pour le
programmeur.

Etant donné que les machines sont indépendantes, la gestion des ressources s'effectue
pour chacune en local. Dans l'approche d'un système distribué, on cherche à pouvoir
gérer le plus finement les ressources au niveau du cluster, et pas uniquement par
un balanceur de charge.

La mise en place de systèmes d'exploitation distribués tels que *DC/OS* est un système
qui se superpose au système d'exploitation de la machine, et qui fournit une gestion
fine des ressources. la :num:`figure #distributedos` permet d'illustrer cette architecture.

.. _distributedos:
.. figure:: images/container_orchestration_revised.png
   :width: 550px
   :align: center
   :alt: Architecture utilisant un outils d'orchestration de containers

   *Architecture utilisant un outil d'orchestration de containers : crédits @ Groovytron*


*DC/OS* est issu de la *Mesosphere*, un ensemble d'outils fournis par Apache qui
répondent spécifiquement aux problématiques du cloud-computing. L'architecture du CHUV
est basée sur les outils de la *Mesossphere*, mais n'utilise pas *DC/OS* au complet.

Les outils utilisés dans le cadre du projet sont décrits dans la suite du document.

Mesos
~~~~~~~~~~~~~~~

Elément central de l'architecture distribuée utilisée au CHUV, *Mesos* :cite:`@mesosdoc` est un noyau
exécuté sur chaque machine du cluster, qui fournit une abstraction des ressources
des machines du cluster. Il est ainsi possible de lancer une application en définissant
la quantité de mémoire vive, le nombre de processeurs, et l'espace disque à disposition,
et Mesos s'occupe de gérer les ressources et la localisation de celles-ci, mais aussi
de gérer le redémarrage de services en cas de pannes, et la mise à l'échelle d'un
service.

Il permet de lancer des applications natives, mais aussi des containers Dockers,
comme c'est le cas dans ce projet.

Le cluster est organisé sous la forme d'un noeud *Master*, et de noeuds *Slaves*.
Le noeud *master* est responsable de recevoir les demandes d'instanciations de services,
et il envoie les ordres aux noeuds *Slaves* approprié, selon les ressources disponibles.
La communication entre le *Master* et les *Slaves* est effectué via *ZooKeeper*, qui
est un système de stockage clé-valeurs dans un système de fichiers, ce qui permet
de partager les configurations des différents acteurs de l'architecture.

Mesos sert donc de support pour l'instanciation de services sur notre architecture distribuée.

Marathon
~~~~~~~~~~~~~~~

*Marathon* est un logiciel développé par *Apache* dans le cadre de la *Mesosphere*.
La Mesosphère est l'ensemble des qui sont utilisés dans le cadre de *DC/OS*, et qui
sont officiellement soutenus par la fondation *Apache*. Marathon joue le rôle de surcouche
à Mesos afin de simplifier le déploiement de **services longues durées**, c'est à
dire qu'une définition de tâche adressée à *Marathon* concerne un certain nombre
d'instances de ce service, et que si une instance vient à se stopper,
*Marathon* va automatiquement relancer une instance de ce service.

Le logiciel fournit lui aussi une *API REST* :cite:`@marathonapidoc`.

Chronos
~~~~~~~~~~~~~~~

*Chronos* est un logiciel développé par la *communauté* Mesos. Cette communauté,
contrairement à la *Mesosphere*, n'est pas officiellement soutenue par *Apache*,
mais est constituée de gens ayant des interêts pour des outils liés à la Mesosphère,
et qui collaborent en suivant le développement des outils de la *Mesosphère*.
La pérénité de ces outils ne sont donc pas garantis.

*Chronos* fait office de remplacement à *cron* de *Linux*, qui est un service permettant
de planifier des commandes à effectuer à intervalles réguliers. Chronos permet d'effectuer
le même travail sur un système distribué via *Mesos*.

Il s'oppose à *Marathon* dans son utilisation, car il permet de lancer une commande
ou un container de manière spontanée, ou programmée, mais qu'il ne cherchera pas à
garder en tout temps un certain nombre d'instances en cours d'exécution.

Il fournit une interface graphique [cf :num:`figure #chronosgui`] permettant de programmer une nouvelle tâche planifiée,
mais aussi une *API REST* permettant l'automatisation programmatique de création de tâches.

.. _chronosgui:
.. figure:: images/chronos_gui.png
   :width: 650px
   :align: center
   :alt: Capture d'écran de l'interface graphique de Chronos

   *Capture d'écran de l'interface graphique de Chronos*

Docker
~~~~~~~~~~~~~~~

*Docker* est une solution *open-source* qui permet d'embarquer une application
dans un container *Linux* qui peut être executé sur n'importe quelle machine.

Dans une deuxième mesure, il fournit des mécanismes pour rendre un container proche
de la virtualisation, en permettant d'isoler les containers entre eux, mais tout en
fonctionnant sur le même système hôte. Ceci a l'avantage par rapport à la virtualisation
de ne pas embarquer le système d'exploitation pour chaque container virtuel, ce qui
réduit la taille des images. En revanche, étant donné que le système d'exploitation
est partagé, et malgré les mécanismes d'isolation entre container et hôte, il est très
difficile d'arriver à un niveau de sécurité identique à celui des machines virtuelles,
qui elles peuvent être sécurisées jusqu'aux niveau des instructions micro-processeurs.

Docker s'utilise généralement pour uniformiser les conditions de développement, car on
peut dire qu'une image fonctionnant en *stand-alone* (c'est à dire sans interactions
avec le système hôte, comme par exemple un montage de volume) doit fonctionner sur une autre instance Docker.

D'un point de vue haut niveau, un container est par défaut isolé de l'hôte au niveau :

* du réseau ;
* du système de fichier ;
* des paquets installés ;
* des services ;
* des utilisateurs.
* des processus (en partie);

Ce qui n'implique pas qu'il est impossible d'accéder à ces différentes instances
de l'hôte, plus ou moins sciemment.

Docker se base sur un système d'image et d'héritage. Il est possible de créer son image
personnalisée à partir d'une image minimale fournie par la communauté comme :

* BusyBox;
* CentOS / Scientific Linux CERN (SLC) on Debian/Ubuntu or on CentOS/RHEL/SLC/etc;
* Debian / Ubuntu;

Mais aussi from scratch, ou via une archive :cite:`@createbaseimagedocker`.

De plus, on peut hériter de n'importe quelle image et la redéfinir via sa propre surcouche.
Les images dont on hérite ne sont pas modifiables. L'héritage est possible pour toute image
publiée sur un dépot d'image Docker (généralement Docker Hub, mais on peut en utiliser d'autres).

La spécialisation du comportement d'un container Docker s'effectue via un fichier de
définition, le `Dockerfile`. Ce fichier est constitué de commandes :cite:`@dockerfilereference`
qui peuvent effectuer des actions pour construire l'image, dont les principales sont :

* Définir de quelle image on hérite;
* Copier un fichier de l'hôte à l'intérieur du système de fichier interne;
* Exécuter une commande bash;
* Définir des variables d'environnements;
* Définir quels ports on veut exposer à l'hôte.

Si on souhaite pouvoir choisir entre plusieurs commande, on peut définir des entrypoints,
qui définissent en général un script que l'on peut exécuter suivant les paramètres d'appels
du container.

Il y a deux méthodes d'intéraction avec un container :

* :code:`docker run`
* :code:`docker exec`

La méthode `run` instancie le container. Il permet de définir des paramètres qui définiront
des caractéristiques internes ou externes du container. Il est par exemple possible de
définir le nom du container, un argument d'entrée (utilisable par l'entrypoint) ou
des variables d'environnement. Suivant l'implémentation du container, il est possible
que celui-ci agisse comme un service, et se maintienne en vie, en attente de nouveaux
événements, ou qu'il se termine dès que le travail interne soit terminé. Dans les deux cas,
il se contente d'attendre que le travail interne(souvent implémenté par un script) renvoie
un code d'erreur :cite:`@codeerrorissue`

La méthode exec ne peut s'appeler que sur un container qui a déjà été instancié.
Si le container est en cours d'exécution, il est possible d'envoyer une nouvelle commande
au container. La plus classique est l'exécution d'un bash en mode interactif, via la commande code:`docker exec -it containername bash`
qui permet d'exécuter une ligne de commande bash. Le paramètre `-it` permet justement
de laisser la commande en mode intéractif, ce qui permet de ne pas fermer l'exécution
de la commande dès que celle-ci renvoie un code `0`.

Il est possible de formuler une description d'architecture composée de containers
*Docker* sous la forme d'un fichier `docker-compose.yml`, qui peut se présenter ainsi :


.. literalinclude:: examples/docker-compose.yml
   :language: yaml

On peut ici voir les configurations de variables d'environnement, de volumes, d'exposition
de ports du container à l'hôte, les versions d'images ainsi que les commandes à
exécuter lorsque le container est prêt.

L'infrastructure peut être lancée via la commande :code:`docker-compose up`. Le fichier
présenté ici ne propose pas de dépendances pour le lancement, ce qui implique que tous
les containers vont tenter de se monter en même temps. Bien qu'une directive :code:`depends-on`
existe pour *docker-compose*, cette option est récente, et ne fonctionne pas à tous les coups.
On préférera utiliser un script *bash* qui s'occupe de démarrer les composants prioritaires
un à un via la commande :code:`docker-compose up nomducomposant`.

Il est intéressant de soulever que *docker-compose* s'occupe seul d'éviter les conflits
de noms de container, contrairement à un démarrage via :code:`docker run`.


Scala
~~~~~~~~~~~~~~~

Ce travail est effectué au cœur du projet Woken du Human Brain Project. Ce projet
contient le langage de programmation Scala :cite:`@scala`. Scala a été concu à l’école polytechnique
de Lausanne (EPFL) afin de proposer de lier des paradigmes de programmation différents
et habituellement opposés, tels que la programmation fonctionnelle et la programmation
orientée objet. Scala se base sur la JVM3, ce qui permet de bénéficier de l’abstraction
de celle-ci en termes de plateforme d’exécution, ainsi que pour la gestion de la mémoire,
notamment. Scala coopère ainsi de manière transparente avec Java, ce qui permet d’utiliser
des bibliothèques non codées en Scala.

Cette section ne précise pas la syntaxique du langage, ni son utilisation.

AKKA
~~~~~~~~~~~~~~~
Akka :cite:`@akka` est un outil de développement et un environnement d’exécution libre et
open-source qui a pour but de simplifier la mise en place d’applications distribuées
et concurrentes basée sur la JVM. Il gère donc les langages de programmations Java et Scala,
et est développé en Scala. Akka propose une résolution des problèmes de concurrence
via un système d’acteurs.

Chaque acteur propose des fonctionnalités, et peut communiquer avec les autres en
envoyant des messages.  Lorsqu’un acteur reçoit un message, il le traite, effectue des
actions et peut envoyer d’autres messages, instancier d’autres acteurs ou encore se stopper.

Chaque acteur est un client léger, qui possède son état et sa boite aux lettres.
Lorsqu’un acteur plante, il est réinstancié automatiquement, dans le même état
qu’il était avant, et avec sa file de message, ce qui procure une haute disponibilité.
De plus, lorsqu’un acteur enfant plante, le parent est notifié, et il peut dès lors
prendre des mesures. Les messages sont asynchrones,ce qui permet de ne pas avoir
d’état bloquant en cas de latence réseau ou tout autre problème technique.
Akka s’occupe de distribuer les acteurs sur le cluster, ce qui permet d’avoir un
haut niveau d’abstraction pour le programmeur.

.. Captain
.. ~~~~~~~~~~~~~~~

.. Captain :cite:`@captain` est un outil qui permet de créer un point


.. _analyse:
Analyse
================

Cette section vise à décrire le cadre logiciel dans lequel le travail sera effectué,
et à préciser les acteurs ainsi que leurs fonctions.

Woken
------------

Woken :cite:`@wokenaxel` est un service, utilisable via une *API REST*, qui fournit la possibilité
d'explorer les données (*data mining* en anglais) de la plateforme. Cette exploration
de données peut être de différentes natures, comme ériger un graphe qui permet
à l'utilisateur de visualiser les données, de demander une analyse statistique,
d'effectuer une expérience de classification via un des algorithmes de classification
fourni, ou encore une expérience de régression.

Chacune de ces explorations de données est effectuée sur un ensemble de données,
qui est qualifié par les champs configurés dans la :num:`Fig. #variables` par l'utilisateur
de la plateforme.

Une expérience fournit des résultats au service demandeur, sous format PFA :cite:`@pfa`,
qui est un format dont la synthaxe est basée sur *yaml*, mais dont la structure est
destinée à décrire des pipeline pour le data-mining.

Des requêtes HTTP sont mises à disposition dans le répertoire :code:`dev-debug/http`
ou :code:`dev-test/http` afin de permettre de se passer de l'interface graphique,
et de simplifier le développement.

Place de Woken dans l'architecture
~~~~~~~~~~~~~~~

Woken étant un service, il est concu pour être utiliser par d'autres services.
La figure :num:`figure #wokenarchiglobal` présente une version simplifiée de l'architecture
de la plateforme MIP.

.. _wokenarchiglobal:
.. figure:: images/woken_archi_global.png
   :width: 350px
   :align: center
   :alt: Architecture globale simplifiée de la plateforme MIP.

   Architecture globale simplifiée de la plateforme MIP. Le **Portal Frontend** est le point d'accès
   pour l'utilisateur. Il peut consulter les données et effectuer des expériences depuis celle-ci.
   Le **Portal Backend** fournit les mécanismes de sécurité et d'accès aux bases de données, ainsi
   que la répartition des demandes à **Woken** si nécessaire. La base de données **Science-db** contient
   les données des patients, tandis que la base de données **Meta-db** contient les descriptions
   de chaque *feature* disponible dans la plateforme. Cette description permet de déterminer différentes
   informations pour la plateforme telles que le type de données (nominale ou continue) ou l'unité de mesure.
   Si il s'agit d'une demande nécessitant un algorithme, c'est **Woken**, l'*algorithm factory*,
   qui va s'occuper de traiter les demandes. **Woken** peut lui-aussi accéder aux bases de données afin
   d'appliquer ses algorithmes. Cette figure est une représentation simplifiée de
   l'architecture, qui ne contient pas tous les intervenants de la plateforme, mais
   uniquement ceux utilisés à cette échelle.

.. raw:: latex

   \clearpage

Lorsque l'utilisateur adresse une requête HTTP contenant une demande d'expérimentation,
le backend envoie une demande de `mining` à woken via une requête POST de la forme :

.. literalinclude:: examples/query-knn.bash
   :language: bash

Ce qui correspond aux paramétrage de l'expérience de l'utilisateur, comme présenté en
:num:`figure #variables`.Woken effectuera traite la requête, effectue l'algorithme et retourne une réponse sous
format *PFA*. Le format de réponse n'est pas important dans le cadre de ce projet.



.. _routesrest:
Il existe deux routes REST pour demander à Woken d'effectuer un travail :

* :code:`/mining/job`
* :code:`/mining/experiment`

Le :code:`/mining/job` permet de lancer un seul algorithme à la fois, et permet pas
de lancer des expériences utilisant la *cross-validation*, tandis que la route :code:`/mining/experiment`
permet la *cross-validation* et de lancer plusieurs algorithmes.

La requête pour une expérience via la route :code:`/mining/experiment` se présente sous la
forme :

.. literalinclude:: examples/query-experiment.sh
   :language: bash

Fonctionnement interne de Woken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Woken a la responsabilité d'appliquer des algorithmes suite à la demande via l'une
des deux :ref:`routes REST <routesrest>` mises à disposition.

La :num:`figure #wokenarchiinternal` présente les intervenants liés à *Woken* lors
d'une demande d'algorithme.

.. _wokenarchiinternal:
.. figure:: images/woken_archi_internal.png
   :width: 600px
   :align: center
   :alt: Architecture  interne de woken.

   Architecture "interne" de woken. Les intervenants ici présents
   sont ceux qui sont directement utilisés par le service *Woken*.
   Le service **Woken** en lui-même est généralement contenu dans un
   container, mais il peut être en natif dans l'architecture, comme dans le cas de l'architecture :code:`dev-debug`
   du projet. Il est responsable d'instancier des **algorithmes** contenus
   dans des containers *Docker*, via *Chronos*. Si l'expérience utilisateur demande une *cross-validation*, un **pool d'acteurs AKKA**
   s'occupant de cette tâche est instanciée au lancement de l'architecture, et sont prêts en tout temps à répondre à cette tâche.
   Ce choix a été effectué afin d'éviter de devoir instancier ces acteurs
   pour chaque demande, en prévision d'une forte charge sur la plateforme. Ces acteurs sont contenus dans un container *Docker*, ce
   qui permet de mettre à l'échelle en cas de besoin. Le résultat de chaque expérience
   est stocké dans la base de données **Woken-DB**, ce qui permet de récupérer
   le fichier de définition *PFA* afin de reconstruire l'éxpérience et de la vérifier,
   si besoin. Attention, les intervenants décrits ci-contre ne sont pas contenus
   dans le projet, mais bel et bien indépendants, et liés via la configuration *Docker-compose*.

Par rapport au code de *Woken*, le principal intervenant est le flux d'acteurs *Akka*,
implémenté dans le script :code:`/src/main/scala/core/coordinator.scala`. C'est celui-ci
qui recoit les expérimentations à effectuer. Celles-ci sont déterminées par un code
d'algorithme, des *features* concernées, les variables cibles ainsi que le modèle et
les hyperparamètres pour les expériences de *machine learning*.

Les acteurs Akka implémentés dans cette portion de code Scala héritent d'une méthodologie
FSM (Finite State Machine), ce qui rend les acteurs capables de se comporter comme un
automate à états finis. Les transition entre ces états s'effectuent via des événements
précis. Cette implémentation permet de mettre un acteur parent en attente des résultats
des acteurs enfants, de manière élégante et sans attente active bloquante.

Suivant la :ref:`route REST <routesrest>` en question, il existe deux flux possibles.

La route :code:`/mining/job` se contente de lancer un `coordinatorActor`, qui est un
acteur responsable de convertir un `Job` (:code:`case class` scala) en JSON mis en
forme selon le format d'entrée de Chronos, de lancer la requête à celui-ci, d'attendre
les résultats dans la base de données *Woken-DB*, de mettre en forme le résultat et
de le retourner au service demandeur.


La voie intéressante dans le cadre de ce projet est celle de :code:`/mining/experiment`.
Celle-ci a pour caractéristiques de pouvoir gérer plusieurs algorithmes pour une expérimentation,
ainsi que de gérer la *cross-validation*.

Le flux de travail entre les acteurs peut être représenté comme montré sur la
:num:`figure #wokenactors`

.. _wokenactors:
.. figure:: images/wokenactors.png
   :width: 650px
   :align: center
   :alt: Schéma des acteurs Akka du script coordinator.scala.

   Schéma des acteurs Akka du script coordinator.scala. Les différents acteurs peuvent
   instancier d'autres acteurs dynamiquement, ce qui permet de répondre à n'importe
   quelle configuration d'expérimentation de l'utilisateur. Ce schéma correspond à
   l'implémentation avant le début du projet. Il existe des `coordinatorActor` qui
   ne sont pas documentés dans ce diagramme. Ils ont pour but d'envoyer un `Job` à
   Chronos, et d'attendre les résultats du container dans la base de données. Ceci
   induit qu'il n'y a pas de communication entre *Woken* et les containers. La cross-validation
   n'est effectuée que si l'algorithme est défini dans *Woken* comme prédictif.
   Les requêtes SQL sont envoyées aux configurations de Chronos (format JSON) sous
   la forme de variables d'environnement. Il est prévu de limiter l'accès aux base
   de données à l'avenir, en passant le dataset aux containers, plutôt que
   de les laisser accéder directement aux bases de données.

Ce flux de travail comporte oblige deux problématiques de taille :


* Il est nécessaire d'attendre un résultat dans la base de données pour que les `localCoordinatorActor` détectent que le container a fourni un travail.
* Il est nécessaire de passer par le mécanisme de *cross-validation* pour définir un score à une expérience. Ceci impose aussi un format *PFA* strict.


Fonctionnement actuel des containers Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Actuellement, les containers utilisés par la plateforme Docker sont lancés via Chronos.
A partir d'une définition d'expérience au format *JSON*, on instancie un objet de définition
de cet algorithme en :code:`case classes` Scala. Depuis ces définitions de classes,
Woken sérialise en `JSON` correspondant au format attendu par Chronos, comme par exemple :

.. literalinclude:: examples/example_chronos.json
   :language: json

Woken est actuellement capable d'instancier autant de containers que demandent les utilisateurs.
Il s'occupe de générer des identifiants uniques comme `id` de tâche à Chronos,
de récolter chacun des résultats dans la base de données et de les mettre en relation avec
la bonne expérience.

Il n'est en revanche pas capable de communiquer avec un container. Une fois le fichier
de configuration `JSON` envoyé via une requête POST HTTP, il ne peut qu'attendre les résultats
dans la base de données.

Dans le cadre de notre nouveau flux, nous devons pouvoir attendre la fin du travail d'un
container, récupérer son résultat, puis adresser une deuxième requête sur le container.

Cette fonctionnalité, que l'on peut qualifier de container "interactifs", doit faire
l'objet de recherches. Docker est conçu pour être *stateless*. Quand un container meurt,
si il n'a pas de *Volume* configuré, le container n'a pas de moyen d'enregistrer l'état
dans lequel il était. Un *Volume* est un répertoire partagé entre le container et l'hôte.
Si il existe des fichiers dans le dossier au moment du montage du *Volume*, le container
y aura accès. Si un le container meurt, le contenu du *Volume* reste.  

Tests préliminaires avec TPOT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Des tests ont été effectués avec TPOT afin de déterminer son efficactié et son utilisabilité.
Dans le cadre de du projet, le plus important était de pouvoir:

* Travailler avec le dataset du projet;
* Pouvoir extraire le meilleure pipeline à la fin de l'optimisation;
* Obtenir les scores;
* Reconstruire le pipeline à partir via Scikit-learn.

Mais aussi, si possible:

* Déterminer les *features* construites;
* Déterminer l'importance de chaque feature.
* Déterminer l'exploitabilité de l'export implémenté dans TPOT.

Des tests :cite:`@tpottests` ont été implémentés, et une issue :cite:`tpotissue` a été
adressée sur le projet afin de vérifier les points délicats.

A la fin de ces tests, il s'avère que :

* Il est possible de récupérer le meilleur pipeline trouvé, avec les hyperparamètres du modèle, ainsi que son score;
* Il est possible d'enregistrer un pipeline sous forme de texte, et de le ré-instancier en objet Scikit-learn utilisable pour des prédictions;
* Tpot n'est pas en mesure de mettre à disposition la selection, la construction et la normalisation de features. Celles-ci sont données par le modèle;
* L'export n'est pas utilisable dans notre contexte;
* Il est possible de travailler via le dataset du projet.

A la fin de cette analyse, les attentes envers TPOT dans le cadre du projet sont atteintes.

Le cas de Marathon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Durant ce projet, la substition de *Chronos* par *Marathon* a été explorée. La raison
est que *Chronos* n'est pas diretement lié à la *Mesosphere*, et que son développement
n'est pas assuré sur le long terme. Une fois intégré dans l'architecture, il s'est avéré que
Marathon ne répond qu'à la problématique des services de longues durées.

*Metronome* :cite:`@metronome` est destiné à être le remplacant de *Marathon*, mais il n'est actuellement
pas assez abouti pour être incorporé à l'architecture.


Conception
============

Cette section ne décrit que les choix de conceptions qui ont étés implémentés.

A partir de l'analyse effectuée au chapitre :ref:`analyse`, il est possible de concevoir
la nouvelle architecture pour résoudre les problèmatiques connues qui sont :

* Mettre en place un flux qui se passe de l'attente des résultats des containers dans la base de données;
* Mettre en place un container qui accepte plusieurs points d'entrées;
* Se passer de la mise en forme de PFA imposée dans le flux actuel.


Modification globale du workflow Woken
------------

Sans parler directement de la modifications des acteurs *Akka*, il est intéressant
de présenter une vue d'ensemble des intervenants dans la problématique du projet,
et de définir les rôles qu'ils remplissent dans cette nouvelle conception.

La :num:`figure #conceptionflow` présente une représentation du flux imaginé.
Elle est volontairement présentée en premier, et avec un haut niveau d'abstraction,
afin de définir la conception des différentes parties qui la constituent. Etant donné
que les restrictions sont fortement liées à Docker et à son fonctionnement, la suite
de la conception est rédigée en parcourant les intervenants de droite à gauche.

.. raw:: latex

   \clearpage

.. _conceptionflow:
.. figure:: images/conceivedworkflow.png
   :width: 400px
   :align: center
   :alt: Schéma du nouveau workflow global.

   Schéma représentant les intéractions entre les différents intervenants, pour la conception retenue.
   Les titres de colonnes définissent la technologie responsable des tâches qui sont
   dans la colonne. Pour le cas d'Akka, cette représentation ne correspond pas à un
   diagramme d'acteur. Ce nouveau flux utilise les *volumes* de Docker afin de faire
   persister les résultats d'entraînements et de prédicats.


Conception pour TPOT
--------------------

Sans se soucier de la problématique *Docker*, le script *Python* doit pouvoir fournir deux
méthodes, :code:`train` et :code:`test`.

La méthode :code:`train` s'occupe de :

* Charger les paramètrages via un fichier *JSON* ;
* Charger le dataset;
* Transformer le dataset pour qu'il soit utilisable par TPOT;
* Séparer le dataset en *training set* et *validation test*;
* Lancer l'entraînement de TPOT avec les données correspondantes;
* Récupérer le meilleur pipeline et l'écrire dans un fichier texte.

La méthode :code:`test` s'occupe de :

* Charger le meilleur pipeline entraîné via un fichier *JSON*;
* Reconstruire le pipeline en objet *Scikit-Learn*;
* Effectuer des prédicats sur les données passées en paramètres;
* Ecrire les scores dans un fichier texte.


Système de containers interactifs
------------

Un container n'est normalement pas conçu pour faire persister des données sur son état.
Lors de l'arrêt d'un container, l'hôte n'enregistre en général pas de données sur son
état avant de l'arrêter. Il est tout de même possible de partager des informations entre
un container et l'hôte via le système de volumes :cite:`@dockervolumes`.

Un volume est un répertoire partagé entre l'hôte et le container. Le lien entre l'hôte
et le container se fait au moment du lancement du container via la commande code:`docker run -v containerpath:hostpath imagename args`.

Si le répertoire contient des fichiers au moment du lien, les fichiers sont directement
accessibles par celui-ci. Le container peut manipuler des fichiers dans ce repertoire
comme il le désire. Une fois le container arrêté, les fichiers crées dans ce répertoire
persistent pour l'hôte.

Partant de ce principe, il est imaginable de créer un container dont le script effectue
un travail différent selon la méthode d'appel, et les fichiers contenus dans le répertoire.

Pour ce faire, il est possible de définir un script qui redirige vers la bonne méthode
du script python en fontion de l'argument `commande` passé en paramètre lors de l'instanciation
du container. Pour rappel, ce paramètre se présente ainsi :code:`docker run parametres nomducontainer commande`.

Une autre méthode explorée (et testée) est de lancer le container dans un mode d'attente,
sans lancer le script, via la commande :code:`docker run containername`, puis de demander
l'exécution d'un entrypoint via la méthode :code:`docker exec containername commande`, où
commande correspond au nom défini dans l'entrypoint.

On connaît déjà à ce stade un **problème** lié à la nature distribuée de l'architecture.
L'utilisation des *volumes* docker utilise un répertoire hôte pour effectuer le lien.
Chronos repose sur Mesos afin de répartir la charge en fonction des ressources, ce qui fait
que l'on ne contrôle pas la machine physique sur laquelle le fichier est crée.
Etant donné qu'il n'y a pas de **système de fichier distribué** dans la plateforme, il
est nécessaire que, pour une expérience, l'appel de l'entraînement et des prédicats
soient effectués sur **la même machine physique**.

Ce problème, bien que connu, n'est pas prioritaire dans le cadre de ce projet. L'utilisation
des *volumes Docker* n'est pas définitive, il est prévu de mettre en place une communication
directe entre l'acteur *Akka* et le container. La principale option semble être la mise
en place d'un système de queues de messages entre l'acteur *Akka* et le container *Docker* lié,
par exemple via une bibliothèque comme ZeroMQ :cite:`zeromq`. Le but de ce projet est
de faire une expérience scientifique sur l'apport de l' *automated machine learning*
dans le cadre de la plateforme.

Chronos
------------------

Chronos est un logiciel que l'on se contentera d'utiliser depuis une
image Docker, il n'y a pas de conception liée à cette partie. Il faut néanmoins
observer précisément le format du JSON à fournir en entrée pour permettre de donner
la configuration complète et correcte pour notre container qui sera lancé.

Il a déjà été vérifié que Chronos, dans sa version `3.0.2`, permet de lancer un
container avec des volumes, des variables d'environnement, et un entrypoint.

Akka
------------------

Le flux d'acteurs présenté à la figure :num:`figure #wokenactors` est modifié afin
de répondre au nouveau container "interactif" lié à Docker. La :num:`figure #newinteractiveactors`
présente le flux de travail alternatif conçu.

.. _newinteractiveactors:
.. figure:: images/modifieddiagramactorscoordinator.png
   :width: 500px
   :align: center
   :alt: Schéma de la nouvelle conception d'acteurs pour le nouveau flux interactif.

   Schéma de la nouvelle conception d'acteurs pour le nouveau flux interactif.
   Un seul acteur suffit à effectuer les deux appels consécutifs du container TPOT.
   Le nouvel acteur commence par définir les conditions d'entraînement pour l'optimisation
   du pipeline dans le cadre de l'expérience. Il doit définir les features, les targets,
   lier les meta-données pour déterminer s'il s'agit d'une expérience de classification
   ou de régression. Le passage via les variables d'environnement des configurations des
   bases de données évitent une configuration trop restrictive en interne au container.
   Les états d'attentes peuvent être implémentés en vérifiant la présence du fichier sur
   le volume ou demander via des requêtes :code:`GET` sur la route du code:`job` de *Chronos*
   l'état de la tâche. La deuxième méthode est recommandée, car elle permet de récupérer
   le code de réussite ou d'erreur de Chronos. La seule présence d'un fichier sur le
   disque ne permet pas de dire si le travail est complet. La mise en forme des prédicats
   pour le retour à l'AlgorithmActor n'est pas encore déterminé.


Implémentation réalisée
============

Cette section précise l'implémentation réalisée dans le cadre de ce projet. Comme toutes
les autres sections, elle ne présente que la version finale, et pas tous les tests et le
cheminement effectués.

Présentation des tâches
------------



Création d'un container interactif
------------

Le `Dockerfile` définit un entrypoint sur un script *bash* personnalisé qui se présente ainsi.


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

TODO:Annexes :
- CdC
- Journal de travail
- TPOT papers
- FULL Rest API for TPOT

.. .. raw:: latex

..  \bibliographystyle{plain}
..  \bibliography{references.bib}

.. bibliography:: references.bib
   :all:
   :style: unsrt

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
