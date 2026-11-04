## Changelog : domifa (30 derniers jours, au 03 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction d'un "mode support", permettant aux administrateurs d'assister les utilisateurs en consultant les interfaces en lecture seule sans risque de modification accidentelle. La sécurité a été considérablement renforcée par l'intégration systématique d'un antivirus pour le scan des fichiers importés et une gestion plus stricte des mots de passe. Enfin, l'interface utilisateur a été modernisée, notamment sur les pages de connexion et de gestion des usagers.

### Évolutions fonctionnelles
- **Introduction du mode support** : mise en place d'un mode de consultation permettant de visualiser les formulaires, les paramètres et les listes d'export sans possibilité de modification ou de désactivation de boutons ([#4334](https://github.com/SocialGouv/domifa/pull/4334), [#4339](https://github.com/SocialGouv/domifa/pull/4339), [#4340](https://github.com/SocialGouv/domifa/pull/4340)).
- **Sécurité des fichiers** : les utilisateurs sont désormais informés en temps réel via le formulaire de contact en cas de détection de menace par l'antivirus.
- **Gestion des accès et mots de passe** : 
    - Mise en place du renouvellement obligatoire du mot de passe après une période d'inactivité.
    - Instauration d'une expiration automatique des mots de passe tous les 60 mois.
    - Possibilité de créer des comptes super-administrateurs via des domaines d'e-mails autorisés.
- **Amélioration de l'interface (UI)** :
    - Refonte visuelle de la page de connexion (en-tête, couleurs et ajout d'un menu déroulant pour choisir le portail).
    - Optimisation de l'alignement des formulaires d'inscription ([#4328](https://github.com/SocialGouv/domifa/pull/4328)).
    - Mise à jour de la navigation et de l'affichage dans la page d'historique ([#4318](https://github.com/SocialGouv/domifa/pull/4318)).
- **Fiabilité des données** : amélioration de la synchronisation de la liste des usagers pour garantir que les informations affichées sont toujours à jour avec le serveur.

### Évolutions techniques
- **Sécurité et protection** :
    - Intégration de ClamAV pour le scan systématique des pièces jointes (formulaire de contact) et des fichiers d'importation des usagers.
    - Renforcement de la validation des fichiers (vérification du type réel avant scan) et limitation de la taille des uploads.
    - Amélioration de la politique de sécurité du contenu (CSP) sur le frontend.
- **Architecture et données** :
    - Migration vers l'utilisation d'identifiants uniques (UUID v7) pour les bénéficiaires et les ayants droit pour une meilleure sécurité.
    - Correction de la gestion des types de données (parsing des entiers) dans les routes et les DTOs pour éviter les erreurs de traitement.
    - Amélioration de la recherche d'usagers et de la gestion des résultats partiels ([#4341](https://github.com/SocialGouv/domifa/pull/4341)).
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement vers Node.js 24.
    - Optimisation des pipelines GitLab CI/CD et de la gestion des images de runtime.

### Autres changements
- Nettoyage des anciennes migrations de base de données déjà appliquées en production.
- Mise à jour du fichier d'actualités (`news.json`).
