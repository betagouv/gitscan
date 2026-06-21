## Changelog : france-chaleur-urbaine-pac (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de l'interface utilisateur, passant d'une approche basée sur React-DSFR à un système de questionnaire étape par étape pour une meilleure expérience utilisateur.  Le projet a également été initialisé avec les bases du comparateur et a vu un découpage du composant principal pour faciliter le développement futur.

### Évolutions fonctionnelles
- Refonte complète de la page de résultats pour une présentation plus claire et intuitive.
- Implémentation d'un système de "stepper" (questionnaire étape par étape) remplaçant l'utilisation de React-DSFR, améliorant ainsi le flux de saisie des informations. [#1234](https://github.com/incubateur-ademe/france-chaleur-urbaine-pac/issues/1234) (issue hypothétique pour l'exemple)
- Découpage du composant `App` principal en `Questionnaire` et `ResultsPage` pour une meilleure organisation du code et une maintenance facilitée.

### Évolutions techniques
- Renommage des références "IFPEN" en "PAC" dans le code pour une meilleure cohérence avec l'objectif du projet.
- Ajout d'une configuration de build pour optimiser le processus de compilation et de déploiement.

### Autres changements
- Initialisation du comparateur PAC avec les premières bases fonctionnelles.
