## Changelog : pitchou (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment au niveau de l'instructeur avec l'ajout de fonctionnalités pour la gestion des pièces jointes, la cartographie, et le contact avec le déposant. Des corrections ont également été apportées pour améliorer la synchronisation des données et la gestion des domaines d'email autorisés. L'administration et le suivi des données ont été renforcés avec l'ajout de statistiques et la gestion des groupes d'instructeurs.

### Évolutions fonctionnelles
- Ajout de la possibilité de contacter le déposant du dossier directement depuis l'interface instructeur. [#627](https://github.com/betagouv/pitchou/issues/627)
- Affichage et téléchargement de la cartographie associée aux dossiers pour les instructeurs. [#629](https://github.com/betagouv/pitchou/issues/629)
- Ajout d'une modale pour la gestion des pièces jointes dans l'interface instructeur. [#634](https://github.com/betagouv/pitchou/issues/634)
- Possibilité d'accepter les fichiers .xlsx pour les espèces protégées. [#628](https://github.com/betagouv/pitchou/issues/628)
- Ajout d'un bouton "Retour" pour faciliter la navigation dans l'interface instructeur. [#609](https://github.com/betagouv/pitchou/issues/609)
- Ajout d'un fil d'Ariane pour améliorer la navigation dans l'application. [#610](https://github.com/betagouv/pitchou/issues/610)
- Affichage d'une erreur claire si l'adresse email utilisée pour la connexion n'est pas autorisée. [#602](https://github.com/betagouv/pitchou/issues/602)
- Ajout de la date de mise en service dans les dossiers (en préparation de la prochaine MEP). [#616](https://github.com/betagouv/pitchou/issues/616)
- Possibilité d'éditer le champ "enjeux" dans l'interface d'instruction. [#604](https://github.com/betagouv/pitchou/issues/604)
- Ajout de la matrice d'impact à la page des statistiques. [#599](https://github.com/betagouv/pitchou/issues/599)
- Ajout de domaines d'email autorisés pour les préfectures (Eure-et-Loir, PACA). [#655](https://github.com/betagouv/pitchou/issues/655), [#641](https://github.com/betagouv/pitchou/issues/641), [#637](https://github.com/betagouv/pitchou/issues/637)

### Évolutions techniques
- Refactorisation de la traduction du schéma de la base de données. [#652](https://github.com/betagouv/pitchou/issues/652)
- Mise en place de Sentry pour la surveillance des erreurs dans les applications instructeur et admin.
- Correction de la sélection GraphQL geometry pour la synchronisation des données. [#632](https://github.com/betagouv/pitchou/issues/632)
- Suppression de l'historique de la date de dernière contribution. [#615](https://github.com/betagouv/pitchou/issues/615)
- Nettoyage du code après la migration vers S3. [#598](https://github.com/betagouv/pitchou/issues/598)
- Suppression des données de synchronisation des "enjeux politiques et écologiques" des annotations privées depuis Démarche Numérique. [#605](https://github.com/betagouv/pitchou/issues/605)
- Refactorisation du code en anglais avec les termes métier français sans accents. [#647](https://github.com/betagouv/pitchou/issues/647)
- Correction du fuseau horaire des dates. [#612](https://github.com/betagouv/pitchou/issues/612)
- Ajout de seeds pour des dossiers plus réalistes. [#608](https://github.com/betagouv/pitchou/issues/608)
- Suppression des personnes n'ayant plus accès à un dossier lors de la synchronisation avec Démarche Numérique. [#625](https://github.com/betagouv/pitchou/issues/625)

### Autres changements
- Ajout de mentions légales pour l'instructeur. [#638](https://github.com/betagouv/pitchou/issues/638)
- Mise à jour des modèles de documents pour la génération de documents. [#614](https://github.com/betagouv/pitchou/issues/614), [#5f8e0f5](https://github.com/betagouv/pitchou/commit/5f8e0f5)
- Mise à jour du délégué à la protection des données (DPO). [#624](https://github.com/betagouv/pitchou/issues/624)
- Ajout de documents via upload. [#640](https://github.com/betagouv/pitchou/issues/640)
- Ajout du groupe instructeur dans le fichier CSV des événements métriques. [#633](https://github.com/betagouv/pitchou/issues/633)
- Ajout du groupe instructeur pour chaque utilisateur dans l'administration. [#633](https://github.com/betagouv/pitchou/issues/633)
- Ajout de seeds pour les dossiers D10 et D11. [#623](https://github.com/betagouv/pitchou/issues/623)
- Correction de la mise à jour de la date des avis. [#653](https://github.com/betagouv/pitchou/issues/653)
- Correction pour que la synchronisation fonctionne en local. (plusieurs tentatives et reverts) [#620](https://github.com/betagouv/pitchou/issues/620)
- Remplacement de "identifiant pitchou" par "numéro dossier" dans les templates de documents et l'API. [#639](https://github.com/betagouv/pitchou/issues/639), [#7303f59](https://github.com/betagouv/pitchou/commit/7303f59)
- Correction du rafraîchissement du dossier en cache. [#648](https://github.com/betagouv/pitchou/issues/648)
- Suppression du lien vers les annotations privées. [#636](https://github.com/betagouv/pitchou/issues/636)
- Correction pour que le déposant soit bien identifié comme le mandataire, même s'il s'agit d'une personne morale. [#650](https://github.com/betagouv/pitchou/issues/650)
- Ajout du suivi d'audience Matomo pour l'instructeur. [#656](https://github.com/betagouv/pitchou/issues/656)
- Activation de la saisie de date typée pour l'instructeur. [#658](https://github.com/betagouv/pitchou/issues/658)
- Correction de la réactivité de la date des prescriptions et de l'UI. [#649](https://github.com/betagouv/pitchou/issues/649)
- Reset de la base de données et de S3 à chaque déploiement en staging. [#621](https://github.com/betagouv/pitchou/issues/621)
