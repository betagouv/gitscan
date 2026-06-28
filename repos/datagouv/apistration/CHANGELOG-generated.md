## Changelog : apistration (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la robustesse de l'API, notamment en renforçant la gestion des accès et en corrigeant des erreurs potentielles. Des améliorations ont également été apportées à la documentation et à l'expérience administrateur, ainsi qu'à la gestion des données TVA et des associations DJEPVA.

### Évolutions fonctionnelles
- Ajout d'un filtre sur le statut des requêtes des fournisseurs dans le tableau de bord administrateur. [#216](https://github.com/datagouv/apistration/issues/216)
- Affichage de l'ID interne de l'utilisateur sur la page de son compte.
- Ajout de la possibilité de filtrer les données TVA par date de publication pour éviter les caches obsolètes. [#223](https://github.com/datagouv/apistration/issues/223)
- Amélioration de la gestion des erreurs pour les associations DJEPVA :
    - Gestion des réponses "not found" de l'API DJEPVA avec un code 404.
    - Mapping des erreurs HTTP 500 de DJEPVA vers des erreurs internes du fournisseur.
    - Acceptation de toutes les familles 922x comme associations sans RNA. [#224](https://github.com/datagouv/apistration/issues/224)
- Ajout de jeux de données de test CNous v4 avec des scénarios INE. [#218](https://github.com/datagouv/apistration/issues/218)
- Intégration de l'API explorer-api-fournisseur skill. [#219](https://github.com/datagouv/apistration/issues/219)
- Ajout d'un cas d'usage pour la TVA avec FranceConnect. [#207](https://github.com/datagouv/apistration/issues/207)
- Ajout de la possibilité de filtrer les endpoints de l'API Entreprise par délégation. [#198](https://github.com/datagouv/apistration/issues/198)
- Ajout d'un lien vers une vidéo explicative dans la FAQ du site. [#165](https://github.com/datagouv/apistration/issues/165)

### Évolutions techniques
- Refonte de la gestion des scopes d'API Particulier :
    - Documentation des scopes et périmètres pour les développeurs.
    - Annotation des scopes sur chaque attribut de réponse de l'API.
    - Affichage des scopes sur chaque fiche d'endpoint de l'API Particulier.
- Suppression du workflow de régénération manuelle du swagger. [#206](https://github.com/datagouv/apistration/issues/206)
- Amélioration de la robustesse des tests : correction d'un test fluctuant lié aux délégations. [#215](https://github.com/datagouv/apistration/issues/215)
- Renforcement de la sécurité des sessions :
    - Expiration des sessions après 12 heures d'inactivité.
    - Limitation de la durée de vie absolue des sessions à 24 heures.
    - Protection contre la fixation de session.
- Ajout d'un suivi des activités des administrateurs pour l'audit. [#163](https://github.com/datagouv/apistration/issues/163)
- Mise à jour des dépendances (Ruby, Rubocop, actions GitHub).
- Suppression de code obsolète (serializer DGFIP situation_ir v2).

### Autres changements
- Mise à jour de la documentation pour l'intégration des éditeurs avec délégation.
- Correction de typos dans le code et la documentation.
- Amélioration du changelog pour les liasses fiscales.
- Changement du lien vers le Bureau Ouvert dans les locales.
- Ajout d'une documentation pour le staging de FranceConnect.
- Suppression des codes de dictionnaire internes dans l'API liasses fiscales v4.
- Ajout d'un identifiant de fournisseur à la page de connexion rapide pour les développeurs.
- Suppression de la liste des tokens des éditeurs dans le formulaire d'édition administrateur.
- Ajout de la possibilité de définir un type de déploiement pour les éditeurs.
- Ajout de seeds pour les éditeurs réels (MGDIS, Atexo, Aiga).
- Amélioration de la gestion des erreurs pour l'API TVA.
- Ajout de la date de dernière mise à jour aux réponses de l'API TVA.
- Suppression de l'utilisation de VIES pour la TVA au profit de DGFIP.
- Ajout de la possibilité de filtrer les requêtes API par délégation.
- Suppression de la commission européenne/numero_tva des cas d'usage.
- Ajout de dgfip/numero_tva à tous les cas d'usage de l'API Entreprise.
