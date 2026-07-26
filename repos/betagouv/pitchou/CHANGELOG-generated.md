## Changelog : pitchou (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Pitchou, notamment en renforçant la sécurité avec l'authentification ProConnect, en améliorant l'interface utilisateur pour les instructeurs (gestion des pièces jointes, affichage de la cartographie, contact du déposeur), et en préparant le terrain pour de futures évolutions (migration vers Tailwind CSS, gestion des domaines d'authentification). Des corrections de bugs et des améliorations de la synchronisation des données ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une page de suivi des événements pour l'administration ([#664](https://github.com/betagouv/pitchou/issues/664)).
- Suivi des clics sur les liens de navigation dans la barre de navigation ([#663](https://github.com/betagouv/pitchou/issues/663)).
- Ajout d'une adresse email de contact dans le pied de page et sur la page 404 ([#661](https://github.com/betagouv/pitchou/issues/661), [#662](https://github.com/betagouv/pitchou/issues/662)).
- Ajout de liens vers les fichiers et Google Drive dans le tableau de bord de l'administration ([#660](https://github.com/betagouv/pitchou/issues/660)).
- Déplacement des pages d'administration vers l'application Admin ([#622](https://github.com/betagouv/pitchou/issues/622)).
- Authentification avec ProConnect pour l'administration ([#613](https://github.com/betagouv/pitchou/issues/613)).
- Amélioration de l'interface pour les instructeurs : affichage de l'entête du dossier, de la ligne demandeur/mandataire ([#654](https://github.com/betagouv/pitchou/issues/654)), nouveaux filtres ([#645](https://github.com/betagouv/pitchou/issues/645)).
- Ajout de guidelines pour la prise de décision CNPN ([#643](https://github.com/betagouv/pitchou/issues/643)).
- Ajout du suivi d'audience Matomo pour les instructeurs ([#656](https://github.com/betagouv/pitchou/issues/656)).
- Activation de la saisie de date typée pour les instructeurs ([#658](https://github.com/betagouv/pitchou/issues/658)).
- Ajout de la possibilité d'autoriser des domaines de préfecture supplémentaires pour l'authentification ([#657](https://github.com/betagouv/pitchou/issues/657), [#655](https://github.com/betagouv/pitchou/issues/655)).
- Affichage et téléchargement de la cartographie pour les instructeurs ([#629](https://github.com/betagouv/pitchou/issues/629)).
- Possibilité de contacter le déposeur du dossier depuis l'entête ([#630](https://github.com/betagouv/pitchou/issues/630)).
- Ajout d'un onglet "Porteur de projet" pour les instructeurs ([#627](https://github.com/betagouv/pitchou/issues/627)).
- Ajout d'une date de mise en service dans le dossier ([#616](https://github.com/betagouv/pitchou/issues/616)).
- Acceptation des fichiers .xlsx pour les espèces ([#628](https://github.com/betagouv/pitchou/issues/628)).
- Ajout de la possibilité d'ajouter des pièces jointes ([#634](https://github.com/betagouv/pitchou/issues/634)).

### Évolutions techniques
- Mise à jour des dépendances Node.js et pnpm ([#666](https://github.com/betagouv/pitchou/issues/666)).
- Utilisation de recettes natives Just pour éviter les exécutions imbriquées redondantes ([#667](https://github.com/betagouv/pitchou/issues/667)).
- Migration vers Tailwind CSS en parallèle du DSFR, avec portage des fichiers ([#665](https://github.com/betagouv/pitchou/issues/665)).
- Refactoring de la page de connexion pour utiliser le modèle DSFR ([#659](https://github.com/betagouv/pitchou/issues/659)).
- Traduction du schéma de la base de données en anglais avec les termes métier français sans accents ([#647](https://github.com/betagouv/pitchou/issues/647)).
- Mise en place de Sentry pour les applications instructeur et admin ([#646](https://github.com/betagouv/pitchou/issues/646)).
- Remplacement de `representative` par `identite_dossier` ([#651](https://github.com/betagouv/pitchou/issues/651)).
- Correction de la sélection GraphQL geometry pour la synchronisation avec Démarches Simplifiées ([#632](https://github.com/betagouv/pitchou/issues/632)).
- Amélioration de la synchronisation avec Démarches Simplifiées ([#620](https://github.com/betagouv/pitchou/issues/620)).

### Autres changements
- Mise à jour du délégué à la protection des données dans la documentation ([#642](https://github.com/betagouv/pitchou/issues/642)).
- Ajout de nouveaux fichiers de saisine CSRPN et de mail de saisine au CNPN.
- Ajout de nouveaux modèles pour la génération de documents.
- Correction d'une erreur d'email de contact sur la page 404 ([#661](https://github.com/betagouv/pitchou/issues/661)).
- Ajout de seeds pour les pièces jointes ([#614](https://github.com/betagouv/pitchou/issues/614)).
- Suppression de la date de dernière contribution dans l'historique ([#615](https://github.com/betagouv/pitchou/issues/615)).
- Nettoyage du code après la migration vers S3 ([#598](https://github.com/betagouv/pitchou/issues/598)).
- Ajout de groupe instructeur dans le fichier CSV des événements métriques ([#633](https://github.com/betagouv/pitchou/issues/633)).
- Ajout de groupe instructeur pour chaque utilisateur ([#633](https://github.com/betagouv/pitchou/issues/633)).
