## Changelog : transport-site (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure technique (Elixir et Phoenix) et un renforcement de la fiabilité des données NeTEx grâce à une couverture de tests accrue. L'interface de gestion (Backoffice) a également bénéficié d'améliorations ergonomiques pour faciliter la recherche et l'utilisation des jeux de données.

### Évolutions fonctionnelles
- **Améliorations du Backoffice** : recherche de datasets plus intuitive [#5633], ajout d'un menu contextuel pour les actions sur les datasets [#5631] et correction du rendu du bouton de validation et du menu contextuel [#5636].
- **Optimisation de l'interface** : amélioration de la mise en page des ressources dans les détails des datasets [#5625] et repositionnement du message invitant au partage des réutilisations [#5638].

### Évolutions techniques
- **Mises à jour majeures** : passage à Elixir v1.20.x [#5612] et convergence vers Phoenix 1.8 (incluant la mise à jour de `phoenix_html` et l'adoption de nouveaux composants de pagination) [#5651, #5646, #5644].
- **Fiabilisation des données NeTEx** : augmentation significative de la couverture de tests (cartes de ressources [#5662], niveaux de sévérité [#5658], rapports de validation [#5650]) et refactorisation du parsing de fichiers Parquet [#5659].
- **Refactorisation du Backoffice** : migration des anciens helpers HTML vers des composants HEEx [#5653] et optimisation de la construction des formulaires [#5656].
- **Qualité logicielle et architecture** : adoption d'une nouvelle stratégie pour les clients HTTP (ADR) [#5648], correction d'alertes Dialyzer [#5652], remplacement de tuples imbriqués par des structures dédiées [#5655] et suppression d'un client d'API obsolète [#5643].
- **Données et performance** : optimisation des imports journaliers par la réutilisation de données en base [#5639] et ajustement du nommage des fichiers GeoJSON convertis [#5645].

### Autres changements
- Remplacement de la bibliothèque Earmark par MDEx pour le rendu Markdown [#5634].
