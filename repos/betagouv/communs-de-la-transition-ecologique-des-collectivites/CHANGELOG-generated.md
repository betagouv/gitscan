## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur la refonte de l'espace "Ressources" avec l'ajout d'une page vocabulaire métier et l'amélioration de la cartographie. Des corrections ont également été apportées pour améliorer la conformité CNIL avec Matomo et résoudre des problèmes de CORS et de proxy. Plusieurs déploiements ont été effectués pour intégrer ces changements.

### Évolutions fonctionnelles
- **Espace Ressources :** Refonte complète de la page vocabulaire selon les maquettes Figma [#378](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/378).
- **Espace Ressources :** Ajout d'un espace "Ressources" avec un proxy pour la cartographie [#367](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/367).
- **Cartographie :** Améliorations de la page d'accueil et du proxy de cartographie [#372](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/372).
- **Statistiques :** Correction d'une erreur CORS sur la page des statistiques [#379](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/379).
- **Statistiques :** Exclusion des catégories de test du dashboard statistiques.
- **Matomo :** Conformité CNIL de Matomo sans bannière de consentement [#377](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/377).
- **Matomo :** Ajout du tracking Matomo sur toutes les pages statiques [#374](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/374).
- **API Projets :** Retrait des badges "nouveau" et renommage de la carte API Projets.
- **Espace Ressources :** Revoir le titre et le sous-titre de l'espace ressources.

### Évolutions techniques
- **Proxy :** Ajout d'un proxy pour analyses-convergence [#373](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/373).
- **Proxy :** Amélioration du proxy pour supporter les attributs HTML avec guillemets simples.
- **Proxy :** Réécriture des chemins dans les fichiers JS proxiés [#373](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/373) et des assets dans le HTML proxié [#368](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/368).
- **Déploiement :** Correction du script `prepare` pour le déploiement Scalingo [#375](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/375).
- **Dépendances :** Déplacement de `openapi-fetch` vers les dépendances [#376](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/376).
- **Ressources :** Remplacement de l'iframe Notion par du contenu statique pour la page Vocabulaire [#378](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/378).

### Autres changements
- Plusieurs releases ont été publiées : 0.1.8, 0.1.9, 0.1.10, 0.1.11, 0.1.12, 0.1.13, 0.1.14, 0.1.15, 0.1.16, 0.1.17, 0.1.18, 0.1.19, 0.1.20, 0.1.21, 0.1.22.
- Correction de l'URL d'embed Notion [#370](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/370).
- Affichage de l'iframe pendant le chargement [#371](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/371).
