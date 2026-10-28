## Changelog : domifa (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a été marqué par l'introduction d'un mode support pour faciliter l'assistance administrative, le renforcement des politiques de sécurité des comptes (gestion des mots de passe, audit des accès) et une modernisation de l'interface utilisateur, notamment sur les pages de connexion et la navigation.

### Évolutions fonctionnelles
- **Nouveau mode support** : déploiement d'un mode permettant aux administrateurs d'assister les utilisateurs avec des restrictions de sécurité (formulaires en lecture seule, désactivation de l'export des données, gestion de sessions de support) ([#4339](https://github.com/SocialGouv/domifa/pull/4339), [#4323](https://github.com/SocialGouv/domifa/pull/4323)).
- **Sécurité et conformité** : 
    - Renforcement de l'audit des accès.
    - Nouvelles politiques de mots de passe : renouvellement forcé après une période d'inactivité, historique des mots de passe et expiration fixée à 60 mois.
- **Expérience utilisateur (UX)** : 
    - Refonte visuelle des pages de connexion (nouveaux en-têtes, logos et menus déroulants).
    - Amélioration de la navigation, notamment dans la page d'historique ([#4318](https://github.com/SocialGouv/domifa/pull/4318)).
    - Mise à jour de la charte graphique (couleurs des boutons et titres).
- **Gestion des usagers** : 
    - Amélioration de la recherche partielle des usagers ([#4341](https://github.com/SocialGouv/domifa/pull/4341)).
    - Amélioration de la gestion des bénéficiaires de famille ([#4291](https://github.com/SocialGouv/domifa/pull/4291)).
- **Administration** : mise à jour des informations de contact et possibilité de créer des super-administrateurs via des domaines d'e-mails autorisés.

### Évolutions techniques
- **Sécurité et données** : 
    - Implémentation des UUID v7 pour les bénéficiaires.
    - Normalisation des données (noms et prénoms) et durcissement des endpoints de l'API usagers.
- **Infrastructure et CI/CD** : 
    - Migration vers Node.js 24.
    - Optimisation des pipelines GitLab CI/CD et des images de runtime.
- **Backend** : 
    - Correction de la gestion des types (parsing des IDs en entiers dans les DTO et paramètres de route).
    - Fiabilisation de la synchronisation des données via le mécanisme `lastSync`.

### Autres changements
- Mise à jour du contenu des actualités de la plateforme.
