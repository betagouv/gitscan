## Changelog : ami-notifications-api (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la modernisation de l'expérience utilisateur et le renforcement de la sécurité. Les principaux changements incluent l'intégration des Passkeys pour une connexion simplifiée, une refonte majeure du système de suivi (followup) pour gérer des contenus plus complexes, et une amélioration de la navigation globale sur l'application.

### Évolutions fonctionnelles
- **Authentification et sécurité :**
    - Introduction du support des Passkeys, incluant une intégration optimisée pour les appareils mobiles iOS et Android [#1088].
    - Amélioration de la gestion de FranceConnect, notamment la correction du processus de déconnexion [#1288, #1241] et une meilleure gestion des erreurs [#1152].
    - Mise en place d'un système de gestion des consentements utilisateurs (stockage et nouveaux points d'accès API) [#911].
- **Expérience utilisateur et interface :**
    - Refonte complète du système de "suivi" (followup) permettant désormais de gérer des structures hiérarchiques complexes avec des sous-éléments [#825].
    - Amélioration de la navigation avec un nouveau comportement pour le bouton "retour" [#1200] et l'ajout d'une vue de reconnexion [#1179].
    - Ajout de nouveaux services (SOS et "Steps") avec des icônes dédiées [#1048].
    - Mise en place de nouveaux composants visuels : carrousels pour les promotions automatiques [#1142, #1001] et une nouvelle checklist [#1140].
    - Corrections diverses sur l'affichage des dates de vacances et des badges [#672, #1203].

### Évolutions techniques
- **Architecture et routage :**
    - Optimisation du routage via l'utilisation de proxies pour les WebSockets [#1292], les fichiers statiques [#1189] et les URLs Django via Vite [#1138].
    - Migration et restructuration de la gestion des partenaires dans l'API [#1131].
- **Sécurité et gestion des données :**
    - Amélioration de la gestion des tokens avec le support du format JWT et l'utilisation de la signature ES256 [#1219].
    - Renforcement de la vérification des signatures pour les jetons FranceConnect [#1172].
- **Qualité et Observabilité :**
    - Intégration de Sentry pour un meilleur suivi des erreurs en production [#1240].
    - Amélioration de la chaîne CI/CD, notamment avec l'ajout de workflows pour les tests iOS et Android [#1176].
    - Unification de la configuration des tests et amélioration de la couverture des tests pour l'agenda et les notifications [#672, #1269].

### Autres changements
- **Nettoyage et maintenance :**
    - Suppression de fichiers d'icônes inutilisés [#445] et de logs de console superflus [#1312].
    - Renommage de la bibliothèque interne `ami-goto` [#1200].
    - Corrections orthographiques et typographiques dans l'interface et la documentation [#1208, #876, #1161].
- **Développement :**
    - Ajout d'une vérification automatique des messages de commit via `pre-commit` [#157].
