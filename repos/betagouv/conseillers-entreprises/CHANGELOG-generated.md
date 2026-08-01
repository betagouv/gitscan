## Changelog : conseillers-entreprises (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de l'expérience utilisateur, notamment autour de la gestion des rapports, des accès et de l'accessibilité. Des optimisations de performance ont également été apportées, ainsi que des corrections de texte et des mises à jour de la documentation.

### Évolutions fonctionnelles
- Ajout d'une interface pour la gestion des clés API utilisateur, incluant la génération et la révocation. [#4605](https://github.com/betagouv/conseillers-entreprises/pull/4605)
- Amélioration de l'affichage des statistiques de correspondance des coopérations en fonction de l'utilisateur connecté. [#4600](https://github.com/betagouv/conseillers-entreprises/pull/4600)
- Affichage des besoins inaccessibles dans l'historique d'une entreprise. [#4550](https://github.com/betagouv/conseillers-entreprises/pull/4550)
- Ajout d'une nouvelle brochure PDF pour le service. [#4603](https://github.com/betagouv/conseillers-entreprises/pull/4603)
- Affichage séparé des gestionnaires de coopération. [#4611](https://github.com/betagouv/conseillers-entreprises/pull/4611)
- Amélioration de l'affichage des rapports pour les sponsors, avec filtrage par antenne. [#4546](https://github.com/betagouv/conseillers-entreprises/pull/4546)
- Ajout d'une API pour les "Subjects" (sujets) avec documentation Swagger et tests. [#4604](https://github.com/betagouv/conseillers-entreprises/pull/4604)

### Évolutions techniques
- Mise à jour de Ruby en version 4.0.6. [#4617](https://github.com/betagouv/conseillers-entreprises/pull/4617)
- Mise à jour de Rails. [#4628](https://github.com/betagouv/conseillers-entreprises/pull/4628)
- Augmentation du nombre de threads Rails et de processus Puma pour améliorer la concurrence. [#4546](https://github.com/betagouv/conseillers-entreprises/pull/4546)
- Ajout de la surveillance du taux de hit du cache AppSignal. [#4627](https://github.com/betagouv/conseillers-entreprises/pull/4627)
- Suppression de scopes inutilisés dans le code. [#4561](https://github.com/betagouv/conseillers-entreprises/pull/4561)
- Optimisation des performances de `Cooperation#with_provenance_details`. [#4600](https://github.com/betagouv/conseillers-entreprises/pull/4600)

### Autres changements
- Améliorations de l'accessibilité avec l'ajout d'attributs ARIA et la correction de la gestion du focus. [#4569](https://github.com/betagouv/conseillers-entreprises/pull/4569)
- Corrections de texte et amélioration de la formulation dans divers endroits de l'application. [#4550](https://github.com/betagouv/conseillers-entreprises/pull/4550), [#4568](https://github.com/betagouv/conseillers-entreprises/pull/4568)
- Mise à jour de diverses dépendances (postcss, svgo, rails-html-sanitizer, loofah).
- Amélioration de la documentation et des métadonnées pour les témoignages. [#4602](https://github.com/betagouv/conseillers-entreprises/pull/4602)
- Suppression de l'ancien layout `user_tabs`. [#4609](https://github.com/betagouv/conseillers-entreprises/pull/4609)
- Ajout de variables d'environnement pour la configuration des emails.
