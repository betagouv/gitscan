## Changelog : drive-migrator (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité des migrations et la visibilité pour l'utilisateur. L'introduction de rapports d'intégrité détaillés permet désormais de vérifier précisément l'état des fichiers migrés, tandis que la gestion des erreurs a été assouplie pour éviter qu'un fichier problématique ne bloque l'ensemble d'un processus.

### Évolutions fonctionnelles
- **Suivi de l'intégrité des données** : mise en place de rapports d'intégrité par fichier et affichage des statistiques de migration (écarts, succès, échecs) directement sur les cartes des espaces de travail et dans l'interface d'administration.
- **Amélioration de la gestion des erreurs** : 
    - Les e-mails de notification incluent désormais un fichier CSV listant les fichiers ayant échoué à la migration.
    - La migration d'un espace de travail ne s'interrompt plus si certains fichiers sont rejetés par le Drive ; ces fichiers sont désormais persistés pour suivi.
    - Réinitialisation automatique des erreurs de l'exécution précédente lors du lancement d'une nouvelle exportation.
- **Optimisation de Resana** : 
    - Meilleure gestion des espaces de travail (verrouillage via `ResanaLockClient`, filtrage par UUID).
    - Restriction de l'accès aux espaces de travail Resana au rôle "Animateur" [#110](https://github.com/suitenumerique/drive-migrator/issues/110) [#160](https://github.com/suitenumerique/drive-migrator/issues/160).
    - Exclusion par défaut des espaces de travail personnels Resana [#163](https://github.com/suitenumerique/drive-migrator/issues/163).
- **Expérience utilisateur et interface** :
    - Mise à jour des logos (ProConnect, en-tête des mails [#221](https://github.com/suitenumerique/drive-migrator/issues/221)).
    - Rendre le menu d'aide (URL de documentation et e-mail de contact) configurable via le backend.
    - Correction du problème de noms de fichiers accentués lors de l'exportation en ZIP.

### Évolutions techniques
- **Modernisation de l'outillage** : adoption de `uv` pour la gestion du projet et l'exécution des workers Celery.
- **Observabilité et Analytics** : intégration poussée de PostHog pour le suivi des connexions utilisateurs, des synchronisations de workspaces et du cycle de vie des migrations.
- **Sécurité et Robustesse** :
    - Mise à jour de Django et PyJWT.
    - Utilisation d'images Docker de base Alpine pour plus de légèreté et de sécurité.
    - Renforcement de la sécurité des partages Drive (restriction aux adresses e-mail exactes).
    - Sécurisation des liens d'exécution dans l'administration (échappement des données utilisateur).
- **Fiabilité des transferts** :
    - Ajout de mécanismes de relance (retry) pour les appels API Drive en cas d'erreurs temporaires (5xx).
    - Passage à l'API "resource server" pour le Drive.
    - Déclaration explicite de la taille des fichiers lors de la création d'items sur le Drive.
- **Infrastructure** : optimisation des images Docker (Nginx, MinIO via Chainguard/Quay.io) et isolation des répertoires de travail pour les tâches d'exportation.

### Autres changements
- **Documentation** : ajout de la documentation concernant les états de vérification d'intégrité et les paramètres PostHog.
- **Qualité logicielle** : amélioration des processus de linting et ajout de tests unitaires sur les redirections d'échec.
