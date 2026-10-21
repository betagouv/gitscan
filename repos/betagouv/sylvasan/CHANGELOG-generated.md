## Changelog : sylvasan (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations majeures sur mobile, notamment pour la prise de photos et la facilité de connexion. L'expérience cartographique a été enrichie par l'ajout d'orthophotos et d'une boussole, tandis que l'interface d'administration gagne en ergonomie avec la gestion des pages par glisser-déposer et une meilleure gestion des permissions par pôle.

### Évolutions fonctionnelles
- **Mobile** : possibilité de s'identifier via l'adresse email ou le nom d'utilisateur [#667](https://github.com/betagouv/sylvasan/pull/667).
- **Mobile** : amélioration de l'expérience photo (gestion des permissions iOS, traitement des erreurs et optimisation de la compression des images).
- **Cartographie** : ajout de la boussole, des orthophotos et ajustement du zoom par défaut sur l'onglet principal [#710](https://github.com/betagouv/sylvasan/pull/710).
- **Cartographie** : accélération du changement de style de carte et amélioration de l'accessibilité des boutons de sélection de style.
- **Administration** : réorganisation de l'ordre des pages par glisser-déposer [#623](https://github.com/betagouv/sylvasan/pull/623) et renommage des référentiels dans la console d'administration [#664](https://github.com/betagouv/sylvasan/pull/664).
- **Permissions** : les administrateurs au niveau d'un pôle peuvent désormais visualiser les réponses qui les concernent [#687](https://github.com/betagouv/sylvasan/pull/687).
- **Formulaires** : ajout de valeurs par défaut pour les champs texte et numérique [#669](https://github.com/betagouv/sylvasan/pull/669) et affichage complet des labels de champs.
- **Corrections** : résolution du bug de duplication de rôles au sein d'une même organisation [#730](https://github.com/betagouv/sylvasan/pull/730), du bug d'affichage de la précision [#671](https://github.com/betagouv/sylvasan/pull/671) et de la disparition de la carte lors du retour de l'application au premier plan.

### Évolutions techniques
- **Mobile** : optimisation des performances Android via l'ajout de règles R8 et mises à jour des versions de l'application.
- **Cartographie** : implémentation d'un nouveau worker Maplibre pour améliorer la gestion des cartes [#668](https://github.com/betagouv/sylvasan/pull/668) et ajout de nouveaux paramètres GPS pour les champs de type carte [#709](https://github.com/betagouv/sylvasan/pull/709).
- **Monitoring** : intégration de Sentry pour le suivi et le rapport d'erreurs sur les interfaces web et mobile [#670](https://github.com/betagouv/sylvasan/pull/670).
- **Backend** : stabilisation de l'ordre des enquêtes retourné par l'API [#665](https://github.com/betagouv/sylvasan/pull/665).
- **Optimisation** : minification du code et refactorisation de la fonction de compression d'images.

### Autres changements
- **Documentation** : ajout d'un ADR (Architecture Decision Record) expliquant les choix concernant les référentiels.
- **Tooling** : mise à jour des outils de pré-commit.
