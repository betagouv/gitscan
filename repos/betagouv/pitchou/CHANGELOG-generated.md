## Changelog : pitchou (30 derniers jours, au 6 juillet 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives en termes de gestion des utilisateurs, de synchronisation des données et d'expérience utilisateur. Des fonctionnalités ont été ajoutées pour faciliter le travail des instructeurs, notamment l'accès aux informations sur les porteurs de projet et la consultation de cartographies. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Les instructeurs peuvent désormais accéder au groupe instructeur associé à chaque utilisateur. [#633](https://github.com/betagouv/pitchou/issues/633)
- Correction de la sélection de géométrie GraphQL dans la synchronisation des données. [#629](https://github.com/betagouv/pitchou/issues/632)
- Les instructeurs peuvent afficher et télécharger la cartographie associée à un dossier. [#629](https://github.com/betagouv/pitchou/issues/629)
- Possibilité de contacter le déposeur du dossier directement depuis l'entête. [#630](https://github.com/betagouv/pitchou/issues/630)
- Ajout d'un onglet "Porteur de projet" pour faciliter l'accès aux informations du demandeur. [#627](https://github.com/betagouv/pitchou/issues/627)
- Ajout de la date de mise en service dans les informations du dossier (en préparation de la prochaine MEP). [#616](https://github.com/betagouv/pitchou/issues/616)
- L'application accepte désormais les fichiers .xlsx pour les espèces. [#628](https://github.com/betagouv/pitchou/issues/628)
- Ajout d'un bouton "Retour" dans la page du dossier. [#609](https://github.com/betagouv/pitchou/issues/609)
- Ajout d'un fil d'Ariane pour faciliter la navigation dans l'application. [#610](https://github.com/betagouv/pitchou/issues/610)
- Les dates de consultation du public sont désormais éditables dans l'onglet instruction. [#600](https://github.com/betagouv/pitchou/issues/600)
- Ajout d'une page d'erreur 404 personnalisée. [#596](https://github.com/betagouv/pitchou/issues/596)
- Amélioration de la section évolution des indicateurs AARRI dans les statistiques. [#597](https://github.com/betagouv/pitchou/issues/597)
- Ajout d'une page utilisateurs dans l'administration avec le niveau AARRI. [#591](https://github.com/betagouv/pitchou/issues/591)
- Migration de la liste des espèces protégées du CSV vers une table en base de données. [#589](https://github.com/betagouv/pitchou/issues/589)
- Correction de l'affichage du fichier espèces impactées après migration vers l'object storage. [#590](https://github.com/betagouv/pitchou/issues/589)
- Ajout d'un bouton pour télécharger les événements utilisateurs pour les statistiques AARRI. [#592](https://github.com/betagouv/pitchou/issues/592)

### Évolutions techniques
- Refactorisation du dépôt en monorepo. [#595](https://github.com/betagouv/pitchou/issues/595) et [#593](https://github.com/betagouv/pitchou/issues/593)
- Correction du chemin du schéma DS pour le worker. [#603](https://github.com/betagouv/pitchou/issues/603)
- Correction du fuseau horaire des dates. [#612](https://github.com/betagouv/pitchou/issues/612)
- Suppression de la synchronisation des "enjeux politique et écologique" (annotation privée) depuis la démarche numérique. [#605](https://github.com/betagouv/pitchou/issues/605)
- Ajout de domaines autorisés pour la connexion (ext.beta.gouv.fr). [#601](https://github.com/betagouv/pitchou/issues/601)
- Correction d'un problème de réinitialisation de l'état "vu" des notifications lors de la resynchronisation. [#592](https://github.com/betagouv/pitchou/issues/592)

### Autres changements
- Mise à jour des modèles pour la génération de documents.
- Ajout de nouveaux fichiers de saisine CSRPN (DREAL ARA) et de mail de saisine au CNPN.
- Ajout de nouveaux types de fichiers de saisine.
- Documentation sur le suivi des événements utilisateurs.
- Suppression de l'historique de la date d'envoi de la dernière contribution.
- Ajout de pièces jointes dans les seeds.
- Correction du format des fichiers CSV pour les statistiques AARRI.
- Suppression de liens vers la démarche numérique dans les dossiers/avis d'expert.
- Correction de bugs liés à la synchronisation avec la démarche numérique en local.
- Suppression de la personne qui suit un dossier si elle n'a pas accès au dossier. [#625](https://github.com/betagouv/pitchou/issues/625)
- Mise à jour du DPO dans la documentation sur les données personnelles. [#624](https://github.com/betagouv/pitchou/issues/624)
- Ajout de seeds (D10 et D11) pour les tests. [#623](https://github.com/betagouv/pitchou/issues/623)
- Ajout de seeds en staging. [#620](https://github.com/betagouv/pitchou/issues/620)
- Remplacement de `db-clear` par `data-clear` pour vider la base de données et le bucket S3. [#615](https://github.com/betagouv/pitchou/issues/615)
- Enrichissement des seeds avec des dossiers plus réalistes. [#608](https://github.com/betagouv/pitchou/issues/608)
