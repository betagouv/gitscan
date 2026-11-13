## Changelog : anssi-portail (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois a été marqué par un enrichissement majeur de la boîte à outils avec l'ajout de nouveaux modèles de documents et une refonte profonde de l'expérience de simulation de hameçonnage. L'accent a également été mis sur la collecte des retours utilisateurs pour améliorer les parcours de sensibilisation et sur une montée de version importante de l'infrastructure technique.

### Évolutions fonctionnelles
- **Simulation de hameçonnage** :
    - Déploiement de nouveaux mini-tests avec des visuels améliorés (cartes animées) et une meilleure adaptation aux mobiles.
    - Mise en place d'un système de score et de collecte des réponses utilisateurs.
    - Création d'un composant Web (WebComponent) permettant d'intégrer facilement les tests de hameçonnage sur des sites externes.
    - Enrichissement du contenu des emails de simulation (Orange, ANSSI, etc.) et amélioration de l'affichage des résultats.
- **Boîte à outils** :
    - Ajout de nouveaux modèles de documents : matrice RACI, revue des droits d'accès, revue des comptes utilisateurs, et listes d'activités.
    - Amélioration de la génération de documents : ajout d'une fonction de prévisualisation des fichiers XLSX, gestion de l'insertion de logos sur les PDF et amélioration du téléchargement.
    - Intégration d'un module de retours utilisateurs directement dans les outils pour recueillir l'avis des professionnels.
- **Parcours de sécurisation** :
    - Mise en place de modales de demande d'avis à des étapes clés (complétion du parcours, obtention du badge Cyberdépart).
- **Annuaires et contacts** :
    - Mise à jour et enrichissement des contacts nationaux, régionaux et sectoriels.
    - Amélioration de l'affichage des cartes de contacts.

### Évolutions techniques
- **Infrastructure et Toolchain** :
    - Migration de la stack vers Node.js 26 et PostgreSQL 18.
    - Mise à jour de l'environnement de développement (Nix, pnpm) et de la configuration CleverCloud.
- **Architecture et Backend** :
    - Implémentation d'un contrat de signalement d'erreurs centralisé pour améliorer la robustesse du système.
    - Réorganisation des routes API (outils, contacts, annuaires et mini-tests) pour une meilleure maintenance.
    - Refactorisation de la logique de manipulation des fichiers Excel (XLSX) et de la gestion des archives.
- **Frontend et UI** :
    - Migration vers la version 2 du kit UI (@lab-anssi/ui-kit).
    - Adoption de nouveaux composants DSFR (Alert, Notice, Upload) pour harmoniser l'interface.
    - Optimisation du rendu serveur (SSR) avec Svelte et amélioration du mode de développement (Hot Reload).

### Autres changements
- **Qualité et Typographie** :
    - Normalisation des espaces typographiques (espaces insécables) dans les fichiers Markdown, HTML et les composants Svelte.
    - Correction de nombreuses coquilles, accents et formulations dans les textes du site.
- **Nettoyage** :
    - Suppression de classes et de modules en doublon ou inutilisés.
    - Optimisation de l'organisation des dossiers du projet.
