## Changelog : seves (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à l'interface utilisateur, notamment en affichant plus d'informations contextuelles (département, nom des établissements) et en optimisant les performances des pages de listes. Des fonctionnalités ont été ajoutées pour faciliter la gestion des documents (export DOCX, téléchargement massif asynchrone) et des communications (ajout de contacts, signatures d'emails). Des corrections de bugs et des améliorations de la sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de l'affichage du département dans plusieurs parties de l'interface utilisateur [#a2ef96d](https://github.com/betagouv/seves/issues/a2ef96d).
- Affichage combiné de l'enseigne et de la raison sociale pour les établissements.
- Possibilité d'exporter les données de Suivi Sanitaire Animal (SSA) au format DOCX [#deefa09](https://github.com/betagouv/seves/issues/deefa09).
- Ajout de la possibilité d'ajouter des agents dans la copie des messages CRDI [#5300ef1](https://github.com/betagouv/seves/issues/5300ef1).
- Amélioration de l'affichage des cartes d'établissements dans SSA [#2ab6dde](https://github.com/betagouv/seves/issues/2ab6dde).
- Ajout d'informations sur l'organisme nuisible pour SSA [#9bebf3c](https://github.com/betagouv/seves/issues/9bebf3c) et [#ddd6739](https://github.com/betagouv/seves/issues/ddd6739).
- Ajout d'un indicateur du nombre de documents, messages et contacts sur les onglets [#ce4143c](https://github.com/betagouv/seves/issues/ce4143c).
- Possibilité de télécharger en masse des documents de manière asynchrone [#269b24d](https://github.com/betagouv/seves/issues/269b24d) et [#92c9174](https://github.com/betagouv/seves/issues/92c9174).
- Ajout des numéros de téléphone des agents dans les signatures d'email [#d7bc3df](https://github.com/betagouv/seves/issues/d7bc3df).
- Ajout de la possibilité d'ajouter des destinataires en copie dans les messages CRDI [#8a89a4b](https://github.com/betagouv/seves/issues/8a89a4b).
- Amélioration de la page de détails pour tous les produits [#180a476](https://github.com/betagouv/seves/issues/180a476).
- Ajout de la date de dernière mise à jour pour TIAC et SSA [#77a5cc5](https://github.com/betagouv/seves/issues/77a5cc5).

### Évolutions techniques
- Intégration de l'outil de linting Biome pour formater le code JavaScript et CSS [#01b6a11](https://github.com/betagouv/seves/issues/01b6a11), [#b257201](https://github.com/betagouv/seves/issues/b257201) et [#6a8f014](https://github.com/betagouv/seves/issues/6a8f014).
- Refactoring du code pour préparer l'implémentation du téléchargement massif asynchrone de documents [#e791f5a](https://github.com/betagouv/seves/issues/e791f5a).
- Mise à jour de plusieurs dépendances (Django, Redis, Ruff, etc.).
- Amélioration des tests pour les établissements [#a37df88](https://github.com/betagouv/seves/issues/a37df88).
- Ajout de GenericRelation dans la vue d'historique pour une meilleure traçabilité [#e5c856e](https://github.com/betagouv/seves/issues/e5c856e).
- Optimisation des performances des listes d'objets TIAC [#7904757](https://github.com/betagouv/seves/issues/7904757).
- Amélioration des logs d'audit [#277cc19](https://github.com/betagouv/seves/issues/277cc19).
- Suppression de l'enregistrement des échecs de connexion dans les logs d'audit [#8e13c1c](https://github.com/betagouv/seves/issues/8e13c1c).

### Autres changements
- Amélioration de la documentation et des messages d'erreur.
- Correction de problèmes de style et d'affichage dans l'interface utilisateur.
- Correction d'une vulnérabilité potentielle dans les liens de rappel conso [#c4de686](https://github.com/betagouv/seves/issues/c4de686).
- Ajout d'une alerte en cas d'utilisation de l'environnement de préproduction [#91dd201](https://github.com/betagouv/seves/issues/91dd201).
- Amélioration des rapports de tests en cas d'échec [#5b61a6f](https://github.com/betagouv/seves/issues/5b61a6f).
- Ajout d'une colonne "état" dans l'export CSV de SV [#45e35a2](https://github.com/betagouv/seves/issues/45e35a2).
- Ajout d'une tâche cron pour l'envoi groupé d'emails [#eedcd9b](https://github.com/betagouv/seves/issues/eedcd9b).
- Amélioration de la vue d'historique et des données historiques [#edacf2a](https://github.com/betagouv/seves/issues/edacf2a) et [#f0c83ff](https://github.com/betagouv/seves/issues/f0c83ff).
- Correction d'un problème de style dans l'export DOCX de SV [#91e9419](https://github.com/betagouv/seves/issues/91e9419).
- Amélioration du filtre pour les agents et les structures dans ICH [#70878ac](https://github.com/betagouv/seves/issues/70878ac).
- Suppression d'un lien dans l'email de transformation pour TIAC [#d07e3ea](https://github.com/betagouv/seves/issues/d07e3ea).
- Ajout de régions et de départements aux structures [#d9fd547](https://github.com/betagouv/seves/issues/d9fd547).
- Autorisation de davantage d'extensions et de types de fichiers pour les documents [#e29061c](https://github.com/betagouv/seves/issues/e29061c).
- Amélioration de l'administration Django [#bc56f6f](https://github.com/betagouv/seves/issues/bc56f6f).
- Correction des tests utilisant l'API Geo [#ff41158](https://github.com/betagouv/seves/issues/ff41158).
- Amélioration de la vue d'historique pour les champs supprimés [#f0c83ff](https://github.com/betagouv/seves/issues/f0c83ff).
- Modification de l'en-tête pour l'IP [#e81dab8](https://github.com/betagouv/seves/issues/e81dab8).
- Amélioration des cartes TIAC [#90c5969](https://github.com/betagouv/seves/issues/90c5969).
- Correction d'un problème de format Biome sur la branche principale [#c70a2bc](https://github.com/betagouv/seves/issues/c70a2bc).
- Ajout de suivi des connexions utilisateurs et des vues de pages [#22309d9](https://github.com/betagouv/seves/issues/22309d9).
- Ajout d'un texte plus clair pour l'export CSV dans les emails HTML [#79cf808](https://github.com/betagouv/seves/issues/79cf808).
- Ajout de notifications après le téléchargement spécifique de documents en batch [#ba5dd46](https://github.com/betagouv/seves/issues/ba5dd46).
- Suppression des éléments en double dans la recherche en texte libre [#9ab795d](https://github.com/betagouv/seves/issues/9ab795d).
- Limitation du nombre de caractères dans le nom de fichier des documents [#f1422bc](https://github.com/betagouv/seves/issues/f1422bc).
- Correction d'un problème de style dans l'export DOCX de SV [#91e9419](https://github.com/betagouv/seves/issues/91e9419).
- Modification de l'ordre des champs de filtre dans TIAC [#95c34ac](https://github.com/betagouv/seves/issues/95c34ac).
- Ajout de la possibilité de filtrer uniquement par date [#89787de](https://github.com/betagouv/seves/issues/89787de).
- Correction d'un bug dans la vue d'historique [#2cd2228](https://github.com/betagouv/seves/issues/2cd2228).
- Amélioration de la valeur de suivi pour les actions EventSimple [#3f07149](https://github.com/betagouv/seves/issues/3f07149).
- Modification du titre des pages de mise à jour TIAC [#91569f7](https://github.com/betagouv/seves/issues/91569f7).
- Ajout du champ "source" comme obligatoire lors de la création pour SSA [#d4a12fc](https://github.com/betagouv/seves/issues/d4a12fc).
- Correction d'un bug lors de la modification d'une investigation TIAC [#4ce803b](https://github.com/betagouv/seves/issues/4ce803b).
