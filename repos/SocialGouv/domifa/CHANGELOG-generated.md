## Changelog : domifa (30 derniers jours, au 13/11/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur trois axes majeurs : le renforcement de l'accessibilité (conformité RGAA), l'extension des capacités d'administration pour les instances régionales (DREETS/DDETS) et la sécurisation accrue des échanges de fichiers via l'intégration systématique de scans antivirus.

### Évolutions fonctionnelles
- **Administration et gestion des comptes** :
    - La DGCS peut désormais gérer les comptes DREETS et DDETS de chaque région ([#4346](https://github.com/SocialGouv/domifa/pull/4346)).
    - Extension des capacités des DREETS : gestion des comptes régionaux et support de nouveaux domaines `.gouv.fr` (Guyane, DRIHL).
    - Ajout d'un menu déroulant de sélection du portail sur les pages de connexion (Admin, Stats, Usagers).
- **Accessibilité (RGAA)** :
    - Travaux importants de mise en conformité : amélioration de l'explicitation des boutons de réinitialisation, des étiquettes de liens de retour et revue générale de l'interface.
- **Expérience utilisateur (UX)** :
    - Mise en place d'un avis de maintenance pour le 19 novembre.
    - Restauration de la possibilité pour les agents et les facteurs de modifier les coordonnées (téléphone et email) des usagers.
    - Amélioration de la synchronisation des listes d'usagers et de la navigation dans l'historique ([#4318](https://github.com/SocialGouv/domifa/pull/4318)).
- **Mode Support** :
    - Encadrement du mode support pour éviter les modifications accidentelles (formulaires en lecture seule, désactivation des boutons d'export usagers).

### Évolutions techniques
- **Sécurité et protection des données** :
    - Renforcement de la sécurité des fichiers : intégration de scans antivirus (ClamAV) sur les imports d'usagers, les pièces jointes du formulaire de contact et les téléchargements de documents.
    - Durcissement des endpoints usagers et contrôle strict des types de fichiers et de la taille des uploads.
    - Optimisation de la politique de sécurité du contenu (CSP) pour la configuration DSFR.
- **Backend et gestion des données** :
    - Normalisation des noms et prénoms lors de la saisie.
    - Amélioration de la robustesse du parsing des identifiants (integers) et de la synchronisation des données (`lastSync`).
    - Augmentation de la limite de référence pour les usagers (de 100 000 à 1 000 000).
- **Infrastructure** :
    - Mise en place d'un service ClamAV local et mise à jour de l'environnement Node.js pour les correctifs de sécurité d'octobre 2026.

### Autres changements
- **Documentation** : Mise à jour des déclarations d'accessibilité suite aux audits RGAA.
- **Développement** : Création d'un marketplace de plugins DomiFa et partage de plugins pour l'aide au développement (Claude Code).
