## Changelog : pitchou (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment dans l'interface instructeur avec l'ajout de fonctionnalités pour la consultation des dossiers (cartographie, porteur de projet, contact du déposeur). Des corrections ont été apportées pour la synchronisation des données et la gestion des domaines autorisés pour l'authentification. Des améliorations ont également été apportées à l'administration et à la documentation.

### Évolutions fonctionnelles
- Ajout de la possibilité de contacter le déposeur du dossier directement depuis l'interface instructeur. [#630](https://github.com/betagouv/pitchou/issues/630)
- Ajout d'un onglet "Porteur de projet" dans l'interface instructeur. [#627](https://github.com/betagouv/pitchou/issues/627)
- Affichage et téléchargement de la cartographie associée au dossier dans l'interface instructeur. [#629](https://github.com/betagouv/pitchou/issues/629)
- Correction de la réactivité de la date des prescriptions et rafraîchissement du dossier en cache dans l'interface instructeur. [#648](https://github.com/betagouv/pitchou/issues/649)
- Ajout d'une modale pour la gestion des pièces jointes dans l'interface instructeur. [#634](https://github.com/betagouv/pitchou/issues/634)
- Possibilité d'éditer les dates de consultation du public dans l'onglet instruction. [#600](https://github.com/betagouv/pitchou/issues/600)
- Possibilité de modifier le champ "enjeux" dans l'onglet instruction. [#604](https://github.com/betagouv/pitchou/issues/604)
- Ajout d'un fil d'Ariane pour faciliter la navigation dans l'application. [#610](https://github.com/betagouv/pitchou/issues/610)
- Ajout d'un bouton "retour" dans l'interface dossier. [#609](https://github.com/betagouv/pitchou/issues/609)
- Affichage des liens des documents associés aux espèces protégées. [#635](https://github.com/betagouv/pitchou/issues/635)
- Ajout de la prise en charge des fichiers .xlsx pour les espèces protégées. [#628](https://github.com/betagouv/pitchou/issues/628)
- Mise à jour des modèles de documents et ajout de nouveaux fichiers de saisine. [#615](https://github.com/betagouv/pitchou/issues/615), [#614](https://github.com/betagouv/pitchou/issues/614)
- Ajout de la possibilité de gérer les groupes d'instructeurs dans l'administration. [#633](https://github.com/betagouv/pitchou/issues/633)
- Ajout de la matrice d'impact à la page des statistiques. [#599](https://github.com/betagouv/pitchou/issues/599)

### Évolutions techniques
- Refactorisation du schéma de la base de données. [#652](https://github.com/betagouv/pitchou/issues/652)
- Mise en place de Sentry pour la surveillance des applications instructeur et admin.
- Remplacement de l'identifiant Pitchou par le numéro de démarche numérique dans divers endroits. [#639](https://github.com/betagouv/pitchou/issues/639)
- Correction du chemin du schéma de synchronisation des données. [#603](https://github.com/betagouv/pitchou/issues/603)
- Amélioration de la synchronisation avec Démarche Numérique, notamment en local.
- Suppression de l'historique de la date de dernière contribution. [#615](https://github.com/betagouv/pitchou/issues/615)
- Nettoyage du code après la migration vers S3. [#598](https://github.com/betagouv/pitchou/issues/598)
- Suppression de la synchronisation des "enjeux politique et écologique" depuis Démarche Numérique. [#605](https://github.com/betagouv/pitchou/issues/605)
- Mise en place d'un reset de la base de données et de S3 sur chaque déploiement en staging. [#621](https://github.com/betagouv/pitchou/issues/621)

### Autres changements
- Ajout de mentions légales pour l'instructeur. [#638](https://github.com/betagouv/pitchou/issues/638)
- Mise à jour de la documentation concernant le délégué à la protection des données. [#642](https://github.com/betagouv/pitchou/issues/642)
- Ajout de domaines PACA et ext.beta.gouv.fr autorisés pour l'authentification. [#641](https://github.com/betagouv/pitchou/issues/641), [#601](https://github.com/betagouv/pitchou/issues/601), [#637](https://github.com/betagouv/pitchou/issues/637)
- Documentation par Audrey Bramy. [#640](https://github.com/betagouv/pitchou/issues/640)
- Correction du fuseau horaire des dates. [#612](https://github.com/betagouv/pitchou/issues/612)
- Ajout de seeds plus réalistes pour les tests. [#608](https://github.com/betagouv/pitchou/issues/608)
- Ajout de seeds pour les pièces jointes. [#614](https://github.com/betagouv/pitchou/issues/614)
- Refactorisation du code en anglais avec termes métier français sans accents. [#647](https://github.com/betagouv/pitchou/issues/647)
- Correction d'un bug où le déposant était incorrectement identifié comme mandataire pour les personnes morales. [#650](https://github.com/betagouv/pitchou/issues/650)
- Suppression du lien vers les annotations privées. [#636](https://github.com/betagouv/pitchou/issues/636)
- Ajout de dossiers D10 et D11 aux seeds. [#623](https://github.com/betagouv/pitchou/issues/623)
- Suppression des personnes n'ayant pas accès à un dossier lors de la synchronisation. [#625](https://github.com/betagouv/pitchou/issues/625)
