## Changelog : playground (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la gestion des workflows, la correction de bugs liés à l'affichage et la sauvegarde des données, ainsi que l'optimisation de l'utilisation des ressources IA. Des améliorations de sécurité et de gestion des utilisateurs ont également été apportées.

### Évolutions fonctionnelles
- Possibilité d'assigner une fiche à un utilisateur pour suivi ([#236](https://github.com/refugies-info/playground/pull/236)).
- Ajout d'une date de fin pour les tableaux d'ingestion, permettant un suivi plus précis des délais ([#232](https://github.com/refugies-info/playground/pull/232)).
- Affichage du nombre de mots dans le tableau d'ingestion pour une meilleure analyse du contenu ([#230](https://github.com/refugies-info/playground/pull/230)).
- Correction d'un bug empêchant la sauvegarde des fiches Bomo ([#243](https://github.com/refugies-info/playground/pull/243)).
- Correction d'un bug lié à l'affichage des titres des fiches RCO en langage clair ([#252](https://github.com/refugies-info/playground/pull/252)).
- Correction d'un bug sur les métadonnées avec des coordonnées GPS ([#253](https://github.com/refugies-info/playground/pull/253)).
- Amélioration de l'affichage du statut de publication des documents.
- Possibilité d'afficher le bouton "enregistrer" même pour les fiches archivées ([#237](https://github.com/refugies-info/playground/pull/237)).
- Ajout de Camille et Jérémy au seed des utilisateurs pour faciliter les tests et le débogage ([#258](https://github.com/refugies-info/playground/pull/258)).
- Activation de la création de nouvelles fiches depuis la sauvegarde ([#254](https://github.com/refugies-info/playground/pull/254)).

### Évolutions techniques
- Mise en place d'une action CI/CD avec Letta Cloud pour la revue de code ([#268](https://github.com/refugies-info/playground/pull/268)).
- Migration de l'identifiant `author_id` vers `assignee_id` dans la table `editorial_records` et les workflows associés ([#257](https://github.com/refugies-info/playground/pull/257), [#238](https://github.com/refugies-info/playground/pull/238), [#242](https://github.com/refugies-info/playground/pull/242)).
- Suppression des paramètres Claude ([#266](https://github.com/refugies-info/playground/pull/266), [#260](https://github.com/refugies-info/playground/pull/260)).
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité ([#262](https://github.com/refugies-info/playground/pull/262)).
- Archivage des anciens assets RCO XML ([#260](https://github.com/refugies-info/playground/pull/260)).
- Ajout d'une commande pour migrer la base de données ([#251](https://github.com/refugies-info/playground/pull/251)).
- Optimisation de l'utilisation de l'IA en limitant la génération de métadonnées aux enregistrements conformes ([#229](https://github.com/refugies-info/playground/pull/229)).
- Suppression d'un workflow Supabase redondant ([#242](https://github.com/refugies-info/playground/pull/242)).

### Autres changements
- Documentation mise à jour concernant l'inventaire Letta Cloud ([#259](https://github.com/refugies-info/playground/pull/259)).
- Correction de références obsolètes dans la documentation ([#260](https://github.com/refugies-info/playground/pull/260)).
- Mise à jour des dépendances de routine.
- Ajustement du cron pour l'ingestion DI.
- Ajout de tests pour les crons.
- Suppression d'un workflow de traduction inutile.
