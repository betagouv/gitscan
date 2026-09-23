## Changelog : hubee (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, hubee a franchi des étapes importantes pour améliorer l'expérience des agents, notamment grâce à une meilleure gestion des pièces jointes (téléchargement facilité) et des outils de recherche de dossiers plus performants. La sécurité a été considérablement renforcée par l'intégration de nouveaux standards d'authentification et l'exigence d'une double authentification (MFA) pour les accès sensibles.

### Évolutions fonctionnelles
- **Gestion documentaire** : 
    - Possibilité de télécharger des pièces reçues ([#163](https://github.com/datagouv/hubee/issues/163)).
    - Amélioration de la visibilité des erreurs lors des échecs de téléchargement ou de remise de pièces.
    - Enrichissement de l'historique avec l'inscription des actions de récupération de pièces.
- **Recherche et navigation** :
    - Recherche de dossiers par numéro (partiel ou complet).
    - Filtrage amélioré permettant de sélectionner plusieurs flux simultanément.
    - Amélioration du tri et de la persistance des filtres dans les listes.
- **Interface utilisateur (Portail)** :
    - Changement de terminologie pour plus de clarté : utilisation du terme "télédossiers" au lieu de "démarches".
    - Affichage des noms de flux à côté de leurs codes pour une meilleure lisibilité.
    - Amélioration de l'affichage des récapitulatifs et de l'historique des changements d'état.
- **Accès** :
    - Possibilité de consulter les dossiers liés à son organisation ([#128](https://github.com/datagouv/hubee/issues/128)).

### Évolutions techniques
- **Sécurité et Authentification** :
    - Mise en place du socle OAuth2 (client_credentials) et support du protocole OIDC avec ProConnect.
    - Renforcement de la sécurité pour les comptes à privilèges via l'exigence d'une authentification multi-facteur (MFA).
    - Amélioration de la gestion des sessions et de la traçabilité des décisions d'accès en base de données.
- **Architecture et API** :
    - Montée de version majeure de la dépendance `hub-api-v1` (passage à la v5.0.0).
    - Refactorisation importante de la gestion des accès (Pundit) et de la logique métier (utilisation d'organizers).
    - Optimisation de la gestion des abonnements via la mise en cache.
- **DevOps et Tests** :
    - Mise en place de "Review Apps" pour tester les modifications directement sur les Pull Requests ([#134](https://github.com/datagouv/hubee/issues/134)).
    - Amélioration de la suite de tests E2E (bout en bout) avec l'utilisation de navigateurs réels.

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API et ajout de guides d'utilisation (runbooks) pour les clients API.
- **Nettoyage** : Suppression de termes et de configurations obsolètes pour simplifier le code.
