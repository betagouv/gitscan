## Changelog : fondation (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes dans le suivi des carrières des magistrats, notamment avec l'ajout de nouveaux outils de visibilité sur les évaluations et les détails de carrière. La gestion documentaire a également été renforcée par l'amélioration de l'éditeur d'agenda et la fiabilisation de la génération de rapports officiels. L'interface utilisateur a été affinée pour offrir une navigation plus fluide et une meilleure accessibilité.

### Évolutions fonctionnelles
- **Gestion des magistrats et évaluations** :
    - Ajout d'une liste permettant d'identifier les magistrats n'ayant pas encore fait l'objet d'une évaluation [#572].
    - Mise en place d'alertes pour les auditions et les évaluations [#559].
    - Création d'une page dédiée aux détails du magistrat [#513].
    - Ajout d'un indicateur de manque d'évaluation sur les dossiers de nomination [#551].
- **Gestion documentaire et agenda** :
    - Déploiement d'un éditeur d'agenda côté client et gestion des éditions de documents [#541, #539].
    - Possibilité de taguer les fichiers joints à une proposition [#562].
    - Amélioration de la gestion des rapports officiels (ordre des fichiers et préparation des sessions) [#538, #548].
- **Améliorations de l'interface (UI/UX)** :
    - Ajout d'alertes concernant les juridictions exclues lors des affectations manuelles [#535].
    - Amélioration de la lisibilité des tableaux (colonnes de statut, infobulles et gestion de l'espace pour les signatures) [#560, #561, #547].
    - Uniformisation de l'affichage des juridictions exclues sur l'ensemble de la plateforme [#570].
    - Correction de l'affichage des auditions sur les dossiers qui n'en acceptent plus [#568].

### Évolutions techniques
- **Architecture et Refactoring** :
    - Refonte des composants de fenêtres modales pour garantir une meilleure accessibilité [#579].
    - Optimisation de la gestion des fichiers et restructuration des routages (layouts et guards de sécurité) [#340, #528, #527].
    - Introduction de `nestjs-cls` pour une meilleure gestion du contexte en backend [#534].
    - Refonte du modèle de vue pour l'éditeur de rapports officiels [#523].
- **Infrastructure et Performance** :
    - Migration de la génération de PDF de Puppeteer vers Gotenberg pour une plus grande fiabilité [#520, #522].
    - Amélioration de la gestion des erreurs lors de la génération de documents via Gotenberg [#573].
- **Qualité et Tests** :
    - Renforcement de la fiabilité avec l'ajout de tests unitaires frontend dans les cycles d'intégration [#544].
    - Utilisation de MSW pour simuler les appels API dans l'environnement Storybook [#557].

### Autres changements
- Mise à jour de la documentation technique (README) et unification des commandes de configuration du projet [#571].
- Optimisation des stories Storybook pour le développement des composants [#569].
