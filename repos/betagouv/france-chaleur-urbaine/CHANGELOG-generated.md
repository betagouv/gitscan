## Changelog : france-chaleur-urbaine (30 derniers jours, au 08/11/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience utilisateur, notamment avec une nouvelle page d'accueil plus intuitive et un espace dédié aux gestionnaires territoriaux (CCRT) entièrement repensé. Le service a également gagné en précision sur les simulations géothermiques et en robustesse grâce à un renforcement des mesures de sécurité et une meilleure synchronisation avec les partenaires (ADEME Connect).

### Évolutions fonctionnelles
- **Nouvelle expérience utilisateur** : Refonte complète de la page d'accueil avec un design plus compact, des outils organisés par onglets et une meilleure visibilité des sections clés [#1343](https://github.com/betagouv/france-chaleur-urbaine/pull/1343).
- **Espace CCRT (Gestionnaires)** : Redesign complet de l'espace dédié aux acteurs territoriaux pour faciliter le suivi, le tri et la gestion des demandes de raccordement.
- **Amélioration des simulations géothermiques** : L'évaluation de la pertinence géothermique est désormais plus précise grâce à l'intégration de nouvelles données (couverture BatEnR, espace de forage) et des messages d'incompatibilité clarifiés.
- **Parcours Chaleur Renouvelable (FCR)** : Optimisation du tunnel de simulation avec un meilleur suivi des étapes et l'ajout de filtres spécifiques pour les sources de chaleur.
- **Outils d'administration** : 
    - Activation de l'export Excel pour les tableaux de gestion.
    - Ajout d'indicateurs pour identifier les écarts de données dans les réseaux de chaleur.
- **Gestion des notifications** : Harmonisation des notifications et possibilité pour les utilisateurs de personnaliser leurs préférences de réception.

### Évolutions techniques
- **Sécurité et Accès** : 
    - Mise en place de l'authentification à deux facteurs (TOTP) pour les comptes administrateurs [#1355](https://github.com/betagouv/france-chaleur-urbaine/pull/1355).
    - Refonte profonde du système de permissions (gestion fine des droits par territoire et par type de demande).
    - Durcissement de la politique de sécurité du contenu (CSP).
- **Intégrations et Données** :
    - Optimisation de la synchronisation avec ADEME Connect (envoi du SIRET, synchronisation des rôles).
    - Suppression définitive de la dépendance technique à Airtable.
    - Migration des données de réseaux et utilisation de la base BDNB pour le calcul du nombre de logements.
- **Performance et Observabilité** :
    - Accélération des tests d'intégration via la parallélisation des processus.
    - Amélioration du tracking analytique (PostHog) pour mieux comprendre le parcours utilisateur.
    - Séparation des environnements de remontée d'erreurs (Sentry) pour isoler les erreurs de production.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique, notamment sur les règles de décision (Publicodes) et les procédures de développement.
- **Nettoyage** : Suppression de commandes CLI obsolètes et de dépendances inutilisées.
