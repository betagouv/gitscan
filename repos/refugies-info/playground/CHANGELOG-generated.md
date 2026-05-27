## Changelog : playground (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion des workflows documentaires, de performance et d'expérience utilisateur. Les principales évolutions concernent l'ajout d'indicateurs de conformité, l'amélioration de la gestion des publications, l'optimisation des recherches et la stabilisation de l'intégration avec l'IA pour la réécriture automatique. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un indicateur de conformité pour les documents, permettant de restreindre l'édition et la publication des contenus non conformes [#229](https://github.com/refugies-info/playground/pull/229).
- Affichage de la date de fin de validité des données dans les tableaux de workflows [#232](https://github.com/refugies-info/playground/pull/232).
- Ajout du nombre de mots dans le tableau d'ingestion [#230](https://github.com/refugies-info/playground/pull/230).
- Ajout d'un indicateur de priorité "urgent" pour les traductions, avec un bouton dédié et une colonne correspondante dans l'interface [#209](https://github.com/refugies-info/playground/pull/209), [#219](https://github.com/refugies-info/playground/pull/219).
- Amélioration de l'affichage des liens de publication avec un popover contenant les URLs et des informations supplémentaires [#208](https://github.com/refugies-info/playground/pull/208).
- Ajout d'un panneau de publication avec des options de confirmation et de partage [#210](https://github.com/refugies-info/playground/pull/210).
- Ajout d'un panneau latéral global pour la navigation et l'accès aux fonctionnalités principales [#204](https://github.com/refugies-info/playground/pull/204).
- Ajout d'un panneau source interactif pour comparer le contenu original et la version réécrite par l'IA [#203](https://github.com/refugies-info/playground/pull/203).

### Évolutions techniques
- Remplacement de la date d'importation par une date d'arbitrage pour un suivi et un tri plus précis des documents [#233](https://github.com/refugies-info/playground/pull/233).
- Optimisation de la gestion des requêtes à l'API Letta pour éviter les limitations de débit [#214](https://github.com/refugies-info/playground/pull/214).
- Amélioration de la gestion de l'état de l'IA lors de la réécriture automatique, avec une reprise possible en cas d'interruption [#211](https://github.com/refugies-info/playground/pull/211).
- Refactorisation du code pour utiliser des composants Radix UI et shadcn/ui, améliorant la cohérence et l'accessibilité de l'interface utilisateur [#217](https://github.com/refugies-info/playground/pull/217).
- Ajout d'un index GIN trigram sur la table `ingestion_records` pour accélérer les recherches [#205](https://github.com/refugies-info/playground/pull/205).
- Utilisation de Zod pour la validation des données côté serveur dans la route `editorial-rewrite` [#209](https://github.com/refugies-info/playground/pull/209).
- Amélioration de la gestion des erreurs et ajout de logs plus précis pour faciliter le débogage [#225](https://github.com/refugies-info/playground/pull/225).
- Mise à jour de la configuration Vercel pour inclure des tâches cron planifiées pour l'ingestion de données [#228](https://github.com/refugies-info/playground/pull/228), [#231](https://github.com/refugies-info/playground/pull/231).

### Autres changements
- Ajout d'une documentation pour l'exportation et l'importation de bases de données Supabase en local [#222](https://github.com/refugies-info/playground/pull/222).
- Correction de problèmes d'autorisation et d'accès aux données dans Supabase [#225](https://github.com/refugies-info/playground/pull/225).
- Suppression des tâches cron d'ingestion de données temporaires [#226](https://github.com/refugies-info/playground/pull/226).
- Nettoyage du code et suppression de composants inutilisés.
- Amélioration de la gestion des erreurs et des logs.
- Correction de bugs mineurs liés à l'interface utilisateur et à la gestion des états.
