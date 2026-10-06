## Changelog : drive-migrator (30 derniers jours, au 05/10/2026)

### Résumé
Cette période est marquée par l'introduction de fonctionnalités cruciales de vérification de l'intégrité, permettant de garantir que les fichiers migrés sont identiques aux sources. L'intégration avec Resana a également été renforcée pour offrir un contrôle plus précis sur les accès et le verrouillage des données pendant les processus de migration.

### Évolutions fonctionnelles
- **Vérification de l'intégrité des données** :
    - Mise en place de rapports détaillés par fichier pour comparer les données migrées avec la source Drive.
    - Affichage des compteurs d'intégrité et des écarts (gaps) directement sur les cartes des espaces de travail et dans l'interface d'administration.
- **Amélioration de l'expérience Resana** :
    - Introduction du verrouillage des espaces de travail et des dossiers pendant la migration pour éviter les conflits.
    - Restriction de l'accès aux espaces de travail Resana au rôle "Animateur" [#110](https://github.com/suitenumerique/drive-migrator/issues/110) [#160](https://github.com/suitenumerique/drive-migrator/issues/160).
    - Exclusion par défaut des espaces de travail personnels Resana [#163](https://github.com/suitenumerique/drive-migrator/issues/163).
- **Interface et communication** :
    - Mise à jour de l'identité visuelle (logos) dans les emails et sur la page de connexion.
    - Rendre les liens d'aide et les adresses de contact configurables via le backend.

### Évolutions techniques
- **Observabilité et Analytics** : Intégration de PostHog pour le suivi des connexions utilisateurs, des synchronisations d'espaces de travail et du cycle de vie des migrations (début/fin).
- **Fiabilité et Robustesse** :
    - Implémentation de tentatives automatiques (retries) lors d'erreurs transitoires de l'API Drive.
    - Isolation des répertoires de travail pour les tâches d'exportation afin d'éviter les interférences.
    - Amélioration de la gestion des noms de fichiers (correction des caractères accentués dans les exports ZIP).
    - Utilisation des UUID au lieu des noms pour le filtrage des rôles et la résolution des slugs Resana.
- **Sécurité et Infrastructure** :
    - Consolidation de nombreux correctifs de sécurité sur les dépendances (frontend, backend et mail).
    - Mise à jour des images Docker (MinIO) vers des sources sécurisées (Chainguard/Quay.io).
    - Optimisation de la CI/CD (Node.js 22, gestion du linting).

### Autres changements
- Documentation des nouveaux états de vérification de l'intégrité de migration.
- Documentation des paramètres de configuration PostHog.
