## Changelog : drive (30 derniers jours, au 07/08/2026)

### Résumé
Les récentes évolutions se concentrent sur une meilleure visibilité du stockage pour les utilisateurs, des fonctionnalités de partage enrichies et un renforcement majeur de la sécurité du système. L'expérience utilisateur est améliorée grâce à une gestion plus claire des quotas et à l'intégration de nouveaux outils de communication.

### Évolutions fonctionnelles
- **Gestion du stockage** : Ajout d'une jauge de stockage visuelle, d'un module de paramètres et de messages d'erreur plus explicites en cas de dépassement de quota.
- **Partage de fichiers** : Possibilité de partager des éléments en masse et d'importer des contacts depuis un fichier pour faciliter les partages.
- **Communication** : Intégration d'un widget de messages accessible directement depuis la page d'accueil ou le menu d'aide.
- **Interface** : Amélioration de la fluidité du modal de partage et mise à jour de l'affichage des tailles de fichiers.

### Évolutions techniques
- **Sécurité** : Renforcement de la protection contre les fichiers malveillants et sécurisation des opérations de renommage et de lecture de fichiers via WOPI. Mise en place d'une liste d'autorisation (allowlist) pour la résolution des fichiers de modèles.
- **Gestion des droits et quotas** : Implémentation d'un nouveau système de gestion des droits (entitlements) incluant des limites de stockage locales, une meilleure gestion du cache et une exposition plus précise des raisons de refus d'upload via l'API.
- **Architecture & API** : Refactorisation de la synchronisation des accès, déplacement de l'endpoint des favoris et ajout d'un endpoint pour le partage groupé d'éléments.
- **Infrastructure** : Durcissement des images Docker et mise à jour des environnements de build (passage à Node 22).

### Autres changements
- Corrections orthographiques sur les messages d'erreur liés aux quotas.
- Synchronisation des traductions pour assurer la cohérence du système.
