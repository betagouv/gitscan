## Changelog : csplab (30 derniers jours, au 2026-06-09)

### Résumé
Ce mois-ci, les évolutions de csplab se concentrent sur l'amélioration de l'ingestion de données (notamment via l'ajout de webhooks Talentsoft), le développement de l'interface utilisateur avec l'introduction d'une nouvelle base de layout et de composants, et l'amélioration de la sécurité avec l'ajout de l'authentification à deux facteurs pour l'administration. Des efforts importants ont également été consacrés à la refactorisation du code et à l'amélioration de la qualité globale du projet.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (2FA) pour l'accès à l'administration Django [#699](https://github.com/betagouv/csplab/issues/699).
- Implémentation de la réception de webhooks Talentsoft pour l'archivage d'offres [#500](https://github.com/betagouv/csplab/issues/500).
- Ajout d'une API pour lister les sources de données [#574](https://github.com/betagouv/csplab/issues/574).
- Ajout d'une API pour récupérer la liste des offres [#440](https://github.com/betagouv/csplab/issues/440).
- Mise en place d'un système de publication de notebook sur GitHub Pages [#641](https://github.com/betagouv/csplab/issues/641).
- Ajout de pages statiques (mentions légales, politique de confidentialité, accessibilité) dans l'interface candidat [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226).
- Amélioration de l'affichage des offres dans l'interface candidat avec l'ajout de composants d'icônes et de boutons [#682](https://github.com/betagouv/csplab/issues/682), [#683](https://github.com/betagouv/csplab/issues/683).
- Création d'une base de layout et d'une barre latérale pour l'interface utilisateur [#701](https://github.com/betagouv/csplab/issues/701).
- Ajout d'un formulaire de base et de composants pour l'ATS (Applicant Tracking System) [#682](https://github.com/betagouv/csplab/issues/682).

### Évolutions techniques
- Refactorisation de l'architecture du domaine (lib-domain) pour une meilleure organisation du code [#663](https://github.com/betagouv/csplab/issues/663), [#672](https://github.com/betagouv/csplab/issues/672).
- Organisation des tests web par couche et par contexte [#673](https://github.com/betagouv/csplab/issues/673).
- Mise en place d'un workflow pour pousser automatiquement les commits sur les branches `main-*` [#659](https://github.com/betagouv/csplab/issues/659).
- Migration vers un modèle utilisateur personnalisé dans Django [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616), [#630](https://github.com/betagouv/csplab/issues/630), [#632](https://github.com/betagouv/csplab/issues/632).
- Refactorisation de l'ingestion pour une meilleure gestion des erreurs et une plus grande robustesse [#509](https://github.com/betagouv/csplab/issues/509).
- Amélioration de la gestion des variables d'environnement pour l'ingestion [#501](https://github.com/betagouv/csplab/issues/501).
- Mise à jour des dépendances (web, ingestion, ocr, notebook) [#675](https://github.com/betagouv/csplab/issues/675), [#676](https://github.com/betagouv/csplab/issues/676), [#677](https://github.com/betagouv/csplab/issues/677), [#678](https://github.com/betagouv/csplab/issues/678).
- Ajout d'un fichier `security.txt` pour signaler les vulnérabilités [#695](https://github.com/betagouv/csplab/issues/695).
- Correction d'un problème de concurrence sur les pages GitHub [#724](https://github.com/betagouv/csplab/issues/724).

### Autres changements
- Ajout de scripts pour s'abonner et supprimer les webhooks Talentsoft [#721](https://github.com/betagouv/csplab/issues/721).
- Ajout d'un workflow pour publier la storybook [#647](https://github.com/betagouv/csplab/issues/647).
- Mise à jour de la documentation pour refléter les changements apportés [#595](https://github.com/betagouv/csplab/issues/595).
- Ajout d'un template de pull request en français [#619](https://github.com/betagouv/csplab/issues/619).
- Correction de problèmes mineurs et améliorations de la qualité du code.
- Ajout d'un workflow pour auto-rebaser les PRs [#718](https://github.com/betagouv/csplab/issues/718).
- Ajout de tests pour le frontend [#716](https://github.com/betagouv/csplab/issues/716).
- Correction de bugs dans l'ingestion des offres [#693](https://github.com/betagouv/csplab/issues/693), [#717](https://github.com/betagouv/csplab/issues/717).
- Ajout d'indexes manquants dans la base de données [#719](https://github.com/betagouv/csplab/issues/719).
