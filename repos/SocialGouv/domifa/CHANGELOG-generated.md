## Changelog : domifa (30 derniers jours, au 09/09/2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'expérience utilisateur, notamment via de nouveaux indicateurs visuels pour le suivi des échéances et l'ajout de ressources comme un kit de communication. Les performances et la stabilité de la plateforme ont également été renforcées grâce à une optimisation du traitement des imports et une meilleure gestion de l'infrastructure.

### Évolutions fonctionnelles
- **Indicateurs de suivi :** Mise en place de pastilles visuelles et de décomptes de jours pour signaler les échéances de passage et de décision des usagers.
- **Nouvelles fonctionnalités :**
  - Ajout d'un onglet "Kit de communication" dans la section FAQ.
  - Intégration d'un formulaire de contact pour le support.
  - Mise à disposition d'un nouveau portail de statistiques.
- **Gestion des comptes :**
  - Les structures peuvent désormais modifier leur adresse email via un processus sécurisé.
  - Amélioration de l'expérience de l'authentification par OTP (ajout d'un compte à rebours de 5 minutes).
- **Navigation et interface :**
  - Redirection automatique des membres des profils DGCS, DDETS et DREETS vers le portail de pilotage lors de la connexion.
  - Renommage du lien "Administration" en "Pilotage" dans la barre de navigation.
- **Corrections :**
  - Rectification des calculs dans les modules de statistiques.
  - Correction des modèles d'emails envoyés par le système.

### Évolutions techniques
- **Optimisation des performances :** Le processus d'importation a été refondu pour utiliser des *worker threads* lors du parsing et de la validation, évitant ainsi de bloquer l'event loop du serveur.
- **Infrastructure et CI/CD :**
  - Routage des requêtes `/import` vers un pod dédié (`backend-export`) pour isoler la charge ([#4249](https://github.com/SocialGouv/domifa/pull/4249)).
  - Amélioration de la résilience des déploiements avec une détection des pods figés pour garantir des mises à jour sans interruption de service.
- **Base de données :**
  - Exécution de migrations pour la mise à jour des comptes utilisateurs ([#4241](https://github.com/SocialGouv/domifa/pull/4241)).
  - Optimisation de la gestion de la concurrence et du nettoyage des fichiers lors des uploads.
- **Sécurité :** Renforcement de la validation et de la sanitisation des données (DTO) pour les processus de mise à jour.

### Autres changements
- **SEO :** Intégration du fichier `robots.txt` dans les assets de build des portails administrateur et statistiques.
- **Maintenance du code :**
  - Standardisation de la gestion des dates via la bibliothèque `date-fns`.
  - Nettoyage de champs de données inutilisés et suppression de migrations obsolètes.
