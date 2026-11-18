## Changelog : mon-service-securise (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois-ci, le développement s'est concentré sur l'automatisation des processus de décision et le renforcement de la gestion des risques. La nouveauté majeure est la capacité de générer automatiquement des supports de présentation PowerPoint complets pour les commissions de sécurité. Parallèlement, l'expérience d'administration a été enrichie avec l'introduction d'un rôle de superviseur et de nouveaux outils de reporting automatique.

### Évolutions fonctionnelles
- **Génération de supports de commission (PowerPoint) :**
    - Automatisation de la création de présentations incluant l'indice cyber (radar et jauges), la cartographie des risques (bruts, à date et cibles), ainsi que le détail des mesures et des pièces du dossier.
    - Ajout de slides de synthèse : plan d'action, proposition de décision, annexes des mesures et avis des membres.
    - Intégration de la gestion des exigences restantes et des statistiques de mesures par catégorie et criticité.
- **Gestion des risques :**
    - Refonte de l'interface de gestion des risques (v2) permettant de lier précisément les risques aux vecteurs et objectifs visés du référentiel ANSSI.
    - Ajout d'une modale dédiée pour la consultation de la liste des risques ANSSI.
- **Administration et pilotage :**
    - Création du rôle de "Superviseur" avec une gestion spécifique des permissions et de la visibilité sur les services.
    - Mise en place de rapports mensuels automatiques pour les administrateurs et superviseurs.
    - Nouveaux tableaux de bord pour suivre l'application des modèles de mesures sur l'ensemble des services.
    - Ajout de préférences de notification (alertes sur les nouveaux services, activation du rapport mensuel).

### Évolutions techniques
- **Optimisations de performance :**
    - Amélioration des requêtes SQL via l'utilisation de sous-requêtes `LATERAL` et l'ajout d'index sur les autorisations et les modèles de mesure.
    - Optimisation du traitement des identifiants par l'utilisation de casts vers le type `UUID`.
- **Architecture et Refactoring :**
    - Modularisation de l'adaptateur PowerPoint en découpant la logique par type de slide pour une meilleure maintenance.
    - Extraction et centralisation du contrôle d'erreurs et des outils de manipulation de documents (texte, formes, nettoyage).
    - Amélioration de la robustesse de l'application par une gestion plus fine des erreurs techniques (notamment pour les services tiers comme ProConnect ou MSS).
- **Infrastructure et Intégration :**
    - Mise à jour des environnements de développement et de production (Node.js v26, PostgreSQL v18).
    - Optimisation des images Docker en allégeant le contexte de build.
    - Renforcement de l'intégration avec le CRM (Twenty) pour la synchronisation automatique des statistiques (nombre de services, nombre d'homologations).
    - Amélioration de la couverture de tests avec l'extension de l'usage de `jsdom`.

### Autres changements
- Nettoyage du code et suppression de fonctions obsolètes.
- Harmonisation de la gestion des logs et de la verbosité selon les environnements.
- Ajustements cosmétiques sur les composants de l'interface (utilisation des cartes du Design System DSFR).
