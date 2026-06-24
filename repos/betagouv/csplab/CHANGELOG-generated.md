## Changelog : csplab (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur pour les recruteurs, notamment l'ajout de fonctionnalités pour la gestion des étapes de recrutement et des organismes. Des améliorations significatives ont également été apportées à l'ingestion des offres, avec une meilleure gestion des sources, des webhooks et des logs. Des travaux d'infrastructure et de tooling ont été réalisés pour améliorer la robustesse et la maintenabilité du projet.

### Évolutions fonctionnelles
- **Recruteur :**
    - Affichage et gestion des étapes de recrutement d'un organisme. [#838](https://github.com/betagouv/csplab/issues/838)
    - Interface pour mettre à jour les étapes d'un organisme. [#835](https://github.com/betagouv/csplab/issues/835)
    - Affinement des catégories d'étapes de recrutement. [#845](https://github.com/betagouv/csplab/issues/845)
- **ATS (Suivi des candidatures) :**
    - Préparation de la barre latérale pour une navigation complète. [#846](https://github.com/betagouv/csplab/issues/846)
    - Ajout d'un composant de tableau générique. [#817](https://github.com/betagouv/csplab/issues/817)
    - Ajout de composants de pagination. [#812](https://github.com/betagouv/csplab/issues/812)
    - Ajout de composants de base (badges, avatars, icônes, boutons). [#682](https://github.com/betagouv/csplab/issues/682), [#741](https://github.com/betagouv/csplab/issues/741)
- **Candidatures :**
    - Implémentation de la soumission de candidature. [#729](https://github.com/betagouv/csplab/issues/729)
    - Affichage du métier dans la liste des offres. [#747](https://github.com/betagouv/csplab/issues/747)
- **Authentification :**
    - Ajout de l'authentification à deux facteurs (2FA) pour l'administration Django. [#699](https://github.com/betagouv/csplab/issues/699)
    - Mise en place de l'authentification par email et mot de passe. [#639](https://github.com/betagouv/csplab/issues/639)
- **Documentation :**
    - Publication du notebook sur GitHub Pages. [#641](https://github.com/betagouv/csplab/issues/641)
    - Rendu de la documentation de l'API en Markdown à l'adresse `/pages/guide_api`. [#820](https://github.com/betagouv/csplab/issues/820)
    - Documentation de l'architecture et des conventions frontend. [#595](https://github.com/betagouv/csplab/issues/595)

### Évolutions techniques
- **Ingestion :**
    - Ajout d'un endpoint pour récupérer une source par UUID. [#837](https://github.com/betagouv/csplab/issues/837)
    - Ajout d'un champ `slug` requis au modèle `Source`. [#837](https://github.com/betagouv/csplab/issues/837)
    - Amélioration de la gestion des webhooks Talentsoft (enregistrement, suppression, traitement asynchrone via Celery). [#694](https://github.com/betagouv/csplab/issues/694), [#737](https://github.com/betagouv/csplab/issues/737)
    - Ajout d'un champ `source_id` aux offres et gestion de la publication des offres vers le web. [#642](https://github.com/betagouv/csplab/issues/642), [#692](https://github.com/betagouv/csplab/issues/692)
    - Gestion de l'archivage des offres. [#824](https://github.com/betagouv/csplab/issues/824)
    - Amélioration de la gestion des erreurs et des logs. [#602](https://github.com/betagouv/csplab/issues/602), [#605](https://github.com/betagouv/csplab/issues/605)
- **Infrastructure :**
    - Sécurisation du déploiement Scalingo en définissant explicitement les variables d'environnement Django. [#839](https://github.com/betagouv/csplab/issues/839)
    - Mise en place d'une sauvegarde quotidienne de la base de données sur Scaleway. [#833](https://github.com/betagouv/csplab/issues/833)
    - Correction de problèmes liés à l'exécution de Huey et de Flower dans des conteneurs Scalingo. [#782](https://github.com/betagouv/csplab/issues/782), [#783](https://github.com/betagouv/csplab/issues/783)
- **Tooling :**
    - Ajout d'un script pour mettre à jour les dépendances. [#832](https://github.com/betagouv/csplab/issues/832)
    - Amélioration des tests (pytest, Cypress).
    - Ajout de workflows GitHub Actions pour l'automatisation des tâches (lint, tests, déploiement).
    - Refactoring des tests et des fixtures.
    - Ajout de vérifications de version dans les workflows CI. [#801](https://github.com/betagouv/csplab/issues/801)

### Autres changements
- Refactoring du code et amélioration de la structure du projet.
- Traduction des erreurs de domaine en français. [#807](https://github.com/betagouv/csplab/issues/807)
- Suppression de code inutile et nettoyage du code.
- Mise à jour des dépendances.
- Ajout d'un fichier `robots.txt` contrôlé par une variable d'environnement. [#810](https://github.com/betagouv/csplab/issues/810)
- Ajout d'un fichier `security.txt`. [#721](https://github.com/betagouv/csplab/issues/721)
- Ajout de composants de notification (CspToast). [#815](https://github.com/betagouv/csplab/issues/815)
- Amélioration de l'accessibilité (a11y) du formulaire de CV. [#464](https://github.com/betagouv/csplab/issues/464)
