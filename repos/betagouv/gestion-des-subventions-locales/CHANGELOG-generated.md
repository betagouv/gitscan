## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la sécurité de l'application, ainsi que sur l'ajout de nouvelles fonctionnalités pour faciliter la gestion des subventions, notamment au niveau des filtres, de l'export de données et de l'affichage d'informations clés sur les projets et les porteurs de projet. Des améliorations significatives ont également été apportées à l'infrastructure de déploiement et aux tests.

### Évolutions fonctionnelles
- Ajout de filtres pour le budget vert, la dotation sollicitée et les dossiers complets sur les listes de projets et de simulations. [#640]
- Ajout de filtres par catégorie DETR/DSIL sur les listes de projets. [#634]
- Ajout de filtres pour le cofinancement, le zonage et la contractualisation. [#642]
- Possibilité de trier les colonnes des tableaux de données. [#597]
- Affichage du prénom et nom du demandeur sur la page projet. [#598]
- Affichage des colonnes "Zonage" et "Contractualisation" dans les tableaux de projets. [#599]
- Ajout de la colonne "Taux sollicité" dans l'export des données. [#636]
- Possibilité d'éditer les commentaires en ligne dans les simulations. [#588]
- Ajout de la civilité du porteur de projet.
- Affichage du montant en lettres.
- Possibilité de programmer les projets acceptés 2026 vers l'enveloppe 2025. [#654]
- Correction : Ne pas re-basculer un projet sur une enveloppe plus récente lors d'une mise à jour de dossier. [#656]
- Correction : Conserver l'enveloppe existante lors de la mise à jour d'un dossier accepté.
- Correction : Affichage correct des cofinancements sur la page projet. [#643]
- Correction : Récupération et affichage de l'arrondissement même s'il n'est pas renseigné. [#592]
- Correction : Formatage correct des nombres dans l'export CSV/ODS/XLS.
- Correction : Problème de réouverture des modales avec du contenu obsolète. [#621]
- Correction : Problème d'affichage des cofinancements sur la page projet. [#643]
- Correction : Problème de hauteur du header pour le taux dans les tableaux. [#602]
- Correction : Problème de toolbar Tiptap. [#605]
- Correction : Problème de barre de recherche sur la page enveloppe du BO. [#603]
- Correction : Problème de synchronisation du montant lors de l'acceptation d'un projet sur Turgot. [#638]
- Correction : Problème de curseur de synchronisation lors d'une erreur d'import de dossier. [#652]
- Correction : Problème de date d'arrêté dans les notifications. [#644]

### Évolutions techniques
- Mise à jour de Django en version 6.0 et migration vers le CSP natif. [#590]
- Amélioration de la performance de la page projet (BO).
- Ajout de tests unitaires et d'intégration pour améliorer la couverture et la qualité du code.
- Refactoring du système de mentions de publipostage. [#632]
- Refactoring des FilterSets et de la pagination de SimulationDetailView.
- Utilisation de SQLite en mémoire pour les tests CI, avec PostgreSQL pour la queue de merge. [#596]
- Amélioration de la suite de tests (accélération d'environ 20%). [#594]
- Ajout d'un workflow de déploiement en production via GitHub Actions. [#647]
- Ajout d'un déploiement de l'environnement de démo. [#653]
- Ajout du scan antivirus ClamAV sur les documents uploadés. [#525]
- Activation du cache-busting pour les fichiers statiques. [#589]
- Refactoring de la gestion des permissions pour les tokens proxy DS.
- Ajout d'un proxy GraphQL pour l'API DS filtré par instructeurs. [#641]
- Ajout d'une configuration pour le schéma GraphQL DS avec autorisation.
- Amélioration de la configuration CI/CD (permissions, jobs parallèles, cache pip).
- Suppression des checksums SRI de django-dsfr.
- Centralisation des événements Matomo dans un fichier de constantes. [#618]

### Autres changements
- Documentation : Ajout d'instructions pour la publication en production.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des dépendances.
- Correction de la bordure entre les lignes de double dotation. [#601]
- Rattrapage de la branche `main`. [#649]
- Backport de `main` dans `develop`. [#646]
- Mise à jour des templates DGCL.
- Ajout d'une action pour déplacer les programmations de projet vers 2025. [#654]
- Ajout d'un script pour sauvegarder le code source chiffré.
- Suppression des URLs de login non utilisés. [#623]
- Mise à jour des noms d'action Matomo. [#604]
- Amélioration du style des filtres. [#587]
- Suppression de la colonne `fr-col` inutile.
- Mise à jour du wording "validé" -> "accepté".
- Ajout de filtres par date sur les listes projets, simulations et programmation. [#625]
