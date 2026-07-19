## Changelog : conseillers-entreprises (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, la performance et la maintenance technique de la plateforme. Des corrections de texte et des ajustements d'affichage ont été apportés pour améliorer l'expérience utilisateur, notamment dans les rapports et l'historique des besoins. L'application a également bénéficié d'une migration technique vers esbuild pour optimiser la compilation des assets JavaScript et d'améliorations de la gestion des emails.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité des champs de formulaire avec des messages d'erreur plus clairs et une navigation au clavier optimisée. [#4569](https://github.com/betagouv/conseillers-entreprises/pull/4569)
- Affichage du pourcentage d'évolution des données dans les tableaux de bord. [#4518](https://github.com/betagouv/conseillers-entreprises/pull/4518)
- Correction de l'affichage des besoins inaccessibles dans l'historique d'une entreprise. [#4550](https://github.com/betagouv/conseillers-entreprises/pull/4550)
- Amélioration de la formulation de certains textes dans les rapports. [#4597](https://github.com/betagouv/conseillers-entreprises/pull/4597)
- Affichage de la date d'envoi des propositions de mise en relation. [#4548](https://github.com/betagouv/conseillers-entreprises/pull/4548)
- Refonte du système d'envoi d'emails avec une gestion des templates plus flexible et une meilleure organisation des traductions. [#4485](https://github.com/betagouv/conseillers-entreprises/pull/4485)

### Évolutions techniques
- Migration de Webpack vers esbuild pour une compilation plus rapide et efficace des assets JavaScript. [#4520](https://github.com/betagouv/conseillers-entreprises/pull/4520)
- Suppression de jQuery et remplacement par des alternatives modernes. [#4542](https://github.com/betagouv/conseillers-entreprises/pull/4542)
- Optimisation de la configuration de la base de données (augmentation du pool de connexions, correction des timeouts). [#4545](https://github.com/betagouv/conseillers-entreprises/pull/4545)
- Amélioration de la gestion de la concurrence avec l'augmentation du nombre de threads Rails et de processus Puma. [#4546](https://github.com/betagouv/conseillers-entreprises/pull/4546)
- Refactorisation du code pour supprimer des scopes inutilisés et simplifier certaines classes. [#4561](https://github.com/betagouv/conseillers-entreprises/pull/4561)
- Amélioration de la robustesse de la gestion des jobs Sidekiq. [#4559](https://github.com/betagouv/conseillers-entreprises/pull/4559)
- Suppression de code JavaScript inutilisé. [#4520](https://github.com/betagouv/conseillers-entreprises/pull/4520)

### Autres changements
- Mise à jour de plusieurs dépendances (undici, concurrent-ruby, nokogiri).
- Amélioration de la documentation et des tests.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout d'un endpoint pour l'accès aux données LLM au format machine-readable. [#4543](https://github.com/betagouv/conseillers-entreprises/pull/4543)
- Correction d'un problème de correspondance des zones territoriales. [#4559](https://github.com/betagouv/conseillers-entreprises/pull/4559)
