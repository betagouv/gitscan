## Changelog : maestro (30 derniers jours, au 17 mars 2026)

### Résumé
Les dernières mises à jour de Maestro apportent des améliorations significatives à la gestion des prélèvements et des programmations, notamment en termes de filtrage, d'affichage des données et de correction de bugs. Des améliorations ont également été apportées à l'export des données et à l'interface utilisateur pour une meilleure expérience globale.

### Évolutions fonctionnelles
- Ajout de filtres par laboratoire sur la liste des prélèvements. [#628](https://github.com/betagouv/maestro/issues/628)
- Affichage de la date du prélèvement et de l'envoi du PV. [#629](https://github.com/betagouv/maestro/issues/629)
- Amélioration de l'affichage des étiquettes de prélèvement et correction du comportement lors de leur génération. [#641](https://github.com/betagouv/maestro/issues/641), [#642](https://github.com/betagouv/maestro/issues/642)
- Ajout de focus sur les champs de recherche pour une meilleure accessibilité. [#643](https://github.com/betagouv/maestro/issues/643)
- Possibilité pour les régions de consulter la répartition des laboratoires. [#571](https://github.com/betagouv/maestro/issues/571)
- Permet aux administrateurs d'accéder à la liste de tous les prélèvements. [#583](https://github.com/betagouv/maestro/issues/583)
- Ajout des champs échantillons après l'envoi du prélèvement. [#593](https://github.com/betagouv/maestro/issues/593)
- Amélioration du suivi des prélèvements avec un nouveau design. [#568](https://github.com/betagouv/maestro/issues/568)
- Correction de l'affichage du destinataire de l'exemplaire dans le suivi. [#575](https://github.com/betagouv/maestro/issues/575)
- Correction de la saisie du type de culture dans le formulaire de prélèvement. [#574](https://github.com/betagouv/maestro/issues/574)
- Correction de la réinitialisation du type de plan suite au téléchargement d'un document vierge. [#573](https://github.com/betagouv/maestro/issues/573)
- Ajout des modalités d'échantillonnage sur le formulaire vierge. [#572](https://github.com/betagouv/maestro/issues/572)

### Évolutions techniques
- Refactor des types de plans DAOA. [#637](https://github.com/betagouv/maestro/issues/637)
- Gestion des types de plan en base de données. [#636](https://github.com/betagouv/maestro/issues/636)
- Suppression de Kafka du projet suite à un changement de protocole. [#595](https://github.com/betagouv/maestro/issues/595)
- Amélioration du typage de l'utilisateur pour éviter l'utilisation de `roles`. [#594](https://github.com/betagouv/maestro/issues/594)
- Remplacement de `fetch-intercept` par un middleware de `rtk query`. [#627](https://github.com/betagouv/maestro/issues/627)
- Suppression de `Openapi` car non utilisé. [#607](https://github.com/betagouv/maestro/issues/607)

### Autres changements
- Correction de bugs liés à l'affichage de la date d'envoi des prélèvements. [#641](https://github.com/betagouv/maestro/issues/641)
- Correction d'un problème de mise à jour d'un échantillon. [#634](https://github.com/betagouv/maestro/issues/634)
- Correction de l'affichage du numéro DAP (12 caractères). [#633](https://github.com/betagouv/maestro/issues/633)
- Correction des laboratoires pour les environnements de tests. [#632](https://github.com/betagouv/maestro/issues/632)
- Suppression des brouillons restants lors de la clôture d'une programmation. [#631](https://github.com/betagouv/maestro/issues/631)
- Ajout des codes manquants sur l'export des prélèvements. [#620](https://github.com/betagouv/maestro/issues/620)
- Correction de l'initialisation des clés GPG. [#615](https://github.com/betagouv/maestro/issues/615)
- Correction des tests trop lents à cause des départements. [#609](https://github.com/betagouv/maestro/issues/609)
- Correction de l'export des prélèvements pour les coordinateurs nationaux. [#611](https://github.com/betagouv/maestro/issues/611)
- Correction de l'affichage du numéro de scellé obligatoire. [#582](https://github.com/betagouv/maestro/issues/582)
- Correction du nombre de prélèvements et des prélèvements exportés pour les profils départementaux. [#578](https://github.com/betagouv/maestro/issues/578)
- Correction du design de l'alerte. [#576](https://github.com/betagouv/maestro/issues/576)
- Correction de l'affichage de la carte d'un prélèvement sans matrice renseignée.
- Correction de l'accès à la liste de tous les prélèvements pour les administrateurs.
- Correction de l'affichage de la page vierge. [#576](https://github.com/betagouv/maestro/issues/576)
- Mise à jour de plusieurs dépendances (mailparser, express-rate-limit, sass, dotenv, helmet, maplibre, vitest, fast-xml-parser).
- Suppression de `highland` et `workbox-webpack-plugin` car non maintenus ou redondants.
- Correction de la version de PostgreSQL utilisée par Scalingo. [#639](https://github.com/betagouv/maestro/issues/639)
- Correction de l'affichage de "Tous" par défaut sur le filtre des laboratoires. [#640](https://github.com/betagouv/maestro/issues/640)
- Scroll automatique en haut de la page sur l'étape 2 du prélèvement. [#619](https://github.com/betagouv/maestro/issues/619)
- Correction de l'ouverture des étiquettes. [#617](https://github.com/betagouv/maestro/issues/617)
- Affichage d'une erreur si le type de fichier est incorrect. [#616](https://github.com/betagouv/maestro/issues/616)
- Correction des champs type de production et type de culture pour la campagne 2026. [#559](https://github.com/betagouv/maestro/issues/559)
