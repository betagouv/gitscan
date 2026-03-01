## Changelog : maestro (30 derniers jours)

### Résumé
Cette mise à jour apporte de nombreuses corrections et améliorations à l'application Maestro, touchant à la gestion des prélèvements, des programmations, des analyses et des utilisateurs. Les modifications visent à améliorer l'expérience utilisateur, corriger des bugs et affiner les droits d'accès en fonction des rôles. Des améliorations techniques ont également été apportées pour optimiser le fonctionnement de l'application et de ses intégrations.

### Évolutions fonctionnelles
- Correction de l'affichage des descripteurs des prélèvements lors de l'export [#581](https://github.com/betagouv/maestro/issues/581).
- Restauration du champ "numéro de scellé" comme obligatoire pour les prélèvements [#582](https://github.com/betagouv/maestro/issues/582).
- Correction du nombre de prélèvements et des prélèvements exportés pour les profils départementaux [#578](https://github.com/betagouv/maestro/issues/578).
- Amélioration de l'affichage du mot de Manon (diminution de la police et gestion des retours à la ligne) [#580](https://github.com/betagouv/maestro/issues/580).
- Possibilité de modifier le champ "saisie" à l'étape 4 du processus de prélèvement [#577](https://github.com/betagouv/maestro/issues/577).
- Correction de l'affichage du destinataire de l'exemplaire dans le suivi des prélèvements [#575](https://github.com/betagouv/maestro/issues/575).
- Correction de la saisie du type de culture (gestion des valeurs vides) [#574](https://github.com/betagouv/maestro/issues/574).
- Ajout des modalités d'échantillonnage sur le formulaire vierge de prélèvement [#572](https://github.com/betagouv/maestro/issues/572).
- Nouvelle interface pour le suivi d'un prélèvement [#568](https://github.com/betagouv/maestro/issues/568).
- Correction des commentaires pour les coordinateurs régionaux dans la gestion des programmations [#570](https://github.com/betagouv/maestro/issues/570).
- Correction des champs "type de production" et "type de culture" pour la campagne 2026 [#559](https://github.com/betagouv/maestro/issues/559).
- Suppression des droits de saisie d'un prélèvement pour un coordinateur régional [#558](https://github.com/betagouv/maestro/issues/558).
- Correction du contenu et des destinataires des notifications lors de la validation de la programmation [#565](https://github.com/betagouv/maestro/issues/565).
- Amélioration de l'affichage des analyses (rattachement à l'échantillon et non au prélèvement) [#553](https://github.com/betagouv/maestro/issues/553).
- Amélioration de l'affichage des indicateurs dans les vues tableau et carte de la programmation [#514](https://github.com/betagouv/maestro/issues/514), [#518](https://github.com/betagouv/maestro/issues/518), [#520](https://github.com/betagouv/maestro/issues/520).
- Amélioration de la recherche d'entreprises.
- Correction de l'affichage des échantillons.
- Correction de la connexion lors de l'utilisation de la mascarade.
- Envoi des notifications de commentaires uniquement aux coordinateurs concernés par les plans [#543](https://github.com/betagouv/maestro/issues/543).
- Correction des libellés de type de production [#516](https://github.com/betagouv/maestro/issues/516).
- Correction du DAP (labos des échantillons et adresse d'envoi au labo trop longue) [#532](https://github.com/betagouv/maestro/issues/532).
- Correction du référentiel PPV 2026 [#536](https://github.com/betagouv/maestro/issues/536).

### Évolutions techniques
- Mise à jour de la librairie Knip [#563](https://github.com/betagouv/maestro/issues/563).
- Mise à jour de la librairie aws-sdk [#556](https://github.com/betagouv/maestro/issues/556).
- Mise à jour de la librairie fast-xml-parser [#527](https://github.com/betagouv/maestro/issues/527).
- Mise à jour de la librairie lodash [#528](https://github.com/betagouv/maestro/issues/528).
- Mise à jour de la librairie workbox [#537](https://github.com/betagouv/maestro/issues/537).
- Mise à jour de la librairie swc [#538](https://github.com/betagouv/maestro/issues/538).
- Amélioration de la gestion des connexions à la base de données PostgreSQL.
- Refactorisation du code pour distinguer l'âge en mois et l'âge en jours [#522](https://github.com/betagouv/maestro/issues/522).
- Amélioration du CI/CD (suppression de l'installation de toutes les dépendances pour les releases) [#552](https://github.com/betagouv/maestro/issues/552).

### Autres changements
- Correction de fautes d'orthographe.
- Suppression de fichiers temporaires après traitement (Sacha) [#544](https://github.com/betagouv/maestro/issues/544).
- Ajout de la version du référentiel Prescripteur (Sacha) [#540](https://github.com/betagouv/maestro/issues/540).
- Ajout de commémoratifs optionnels (Sacha) [#562](https://github.com/betagouv/maestro/issues/562), [#550](https://github.com/betagouv/maestro/issues/550).
- Mise à jour de la référence Inovalys [#561](https://github.com/betagouv/maestro/issues/561).
- Ajout d'une ligne pour les consignes de répartition dans la programmation [#529](https://github.com/betagouv/maestro/issues/529).
- Suppression de l'obligation du numéro de scellé pour le plan de surveillance [#524](https://github.com/betagouv/maestro/issues/524).
- Initialisation des échantillons en fonction de la programmation [#531](https://github.com/betagouv/maestro/issues/531).
- Suppression du filtre départements pour certains rôles [#535](https://github.com/betagouv/maestro/issues/535).
- Correction de l'accès à la programmation départementale pour certains utilisateurs [#513](https://github.com/betagouv/maestro/issues/513).
- Affichage uniquement des préleveurs rattachés au plan [#525](https://github.com/betagouv/maestro/issues/525).
