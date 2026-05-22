## Changelog : playground (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'amélioration de la gestion des documents, notamment en affinant le processus d'ingestion, en améliorant l'interface utilisateur pour la publication et la traduction, et en renforçant la robustesse de l'application. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une date d'arbitrage pour le suivi et le tri des documents [#233](https://github.com/refugies-info/playground/issues/233).
- Affichage de la date de fin dans les tableaux de données. [#232](https://github.com/refugies-info/playground/issues/232)
- Ajout du nombre de mots dans le tableau d'ingestion. [#230](https://github.com/refugies-info/playground/issues/230)
- Possibilité d'activer/désactiver la génération automatique de métadonnées non conformes. [#229](https://github.com/refugies-info/playground/issues/229)
- Ajout d'un indicateur de priorité "urgent" pour les traductions, avec un nouveau bouton et une colonne correspondante dans l'interface. [#221](https://github.com/refugies-info/playground/issues/221), [#219](https://github.com/refugies-info/playground/issues/219), [#218](https://github.com/refugies-info/playground/issues/218)
- Amélioration de l'affichage des liens de publication avec un popover contenant les URLs. [#217](https://github.com/refugies-info/playground/issues/217), [#208](https://github.com/refugies-info/playground/issues/208)
- Ajout d'un filtre par type d'entrée dans la liste des documents. [#198](https://github.com/refugies-info/playground/issues/198)
- Correction des labels des modalités d'entrée/sortie. [#200](https://github.com/refugies-info/playground/issues/200), [#199](https://github.com/refugies-info/playground/issues/199)
- Ajout d'une barre latérale globale persistante pour la navigation. [#206](https://github.com/refugies-info/playground/issues/206), [#205](https://github.com/refugies-info/playground/issues/205), [#204](https://github.com/refugies-info/playground/issues/204)
- Refonte de l'en-tête de la fiche avec ajout d'une indication de sauvegarde et d'un bouton de copie du lien. [#203](https://github.com/refugies-info/playground/issues/203), [#202](https://github.com/refugies-info/playground/issues/202)

### Évolutions techniques
- Refactorisation de la gestion de la génération de métadonnées pour optimiser l'utilisation de l'IA. [#228](https://github.com/refugies-info/playground/issues/228)
- Amélioration de la gestion des versions d'ingestion pour éviter la duplication des workflows.
- Mise en place d'un système de cron jobs pour l'ingestion de données, avec une planification flexible. [#227](https://github.com/refugies-info/playground/issues/227), [#215](https://github.com/refugies-info/playground/issues/215), [#214](https://github.com/refugies-info/playground/issues/214)
- Correction de problèmes d'autorisation et de permissions sur la base de données. [#226](https://github.com/refugies-info/playground/issues/226), [#225](https://github.com/refugies-info/playground/issues/225)
- Optimisation des requêtes SQL avec l'ajout d'index GIN. [#201](https://github.com/refugies-info/playground/issues/201)
- Amélioration de la gestion des erreurs et de la journalisation.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Utilisation de `Object.hasOwn` pour des vérifications de propriétés plus sûres. [#197](https://github.com/refugies-info/playground/issues/197)

### Autres changements
- Ajout d'une documentation pour l'export et l'import de bases de données Supabase. [#222](https://github.com/refugies-info/playground/issues/222)
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour des dépendances.
