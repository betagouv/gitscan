## Changelog : drive (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la gestion de l'espace de stockage et la simplification du partage de fichiers. Les utilisateurs bénéficient désormais d'outils plus visuels pour suivre leur quota et de méthodes plus rapides pour partager des documents (partage groupé, importation de contacts). Parallèlement, une attention particulière a été portée à la sécurité, notamment sur les opérations de modification de fichiers et la robustesse de l'infrastructure.

### Évolutions fonctionnelles
- **Gestion du stockage et des quotas** :
    - Ajout d'une jauge de stockage visuelle et d'un modal de configuration pour suivre l'utilisation de l'espace.
    - Amélioration de l'expérience utilisateur lors du dépassement de quota avec des messages d'erreur plus explicites.
    - Mise à jour automatique de la jauge de stockage lors des actions de déplacement ou de duplication de fichiers.
    - Possibilité d'exclure certains éléments du calcul du quota de stockage.
- **Amélioration du partage** :
    - Introduction du partage d'éléments en masse (batch share).
    - Possibilité de partager un élément avec des contacts importés directement depuis un fichier.
- **Interface utilisateur** :
    - Intégration du widget de messages sur la page d'accueil et via le menu d'aide pour un accès plus rapide.
    - Correction d'un bug empêchant la fermeture correcte du modal de partage lors d'événements de glisser-déposer.

### Évolutions techniques
- **Sécurité et conformité** :
    - Renforcement de la sécurité des opérations via WOPI (analyse systématique des fichiers écrits et rejet des cibles de renommage non sécurisées).
    - Durcissement de la sécurité des images Docker et mise en place d'une liste blanche pour la résolution des fichiers de modèles.
    - Amélioration de la gestion de la détection de malwares (suppression automatique des enregistrements lors de la purge d'un fichier).
- **Architecture Backend** :
    - Implémentation d'un nouveau système local de gestion des droits (entitlements) incluant des limites de stockage par utilisateur.
    - Refactorisation de la synchronisation des accès des descendants vers un service dédié.
    - Optimisation de la gestion du cache de stockage pour garantir la cohérence des données lors des écritures.
    - Migration de l'API des favoris vers un nouvel endpoint (`/items/favorites/`).
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de build vers Node 22 pour plusieurs processus (workflows de traduction, construction des mails).
    - Mise à jour des images de base (Alpine 3.24) et optimisation des Dockerfiles.

### Autres changements
- Correction de fautes d'orthographe dans les messages d'erreur relatifs aux quotas.
- Mise à jour de la documentation du changelog.
