## Changelog : synapse-room-access-rules (30 derniers jours, au 27 mai 2026)

### Résumé
Les récentes mises à jour de `synapse-room-access-rules` améliorent la gestion de l'accès aux salles, notamment en introduisant la notion de visibilité (publique/privée) et en corrigeant des problèmes liés à la création de salles chiffrées ou non chiffrées. Ces changements renforcent la flexibilité et la sécurité de l'accès aux conversations.

### Évolutions fonctionnelles
- Ajout de la gestion de la visibilité des salles (publique ou privée) via le paramètre `visibility` dans les règles d'accès. [#18](https://github.com/tchapgouv/synapse-room-access-rules/issues/18)
- Support des salles privées non chiffrées. [#18](https://github.com/tchapgouv/synapse-room-access-rules/issues/18)
- Correction : Les paramètres `force_unencrypted_at_creation` et `visibility` sont maintenant optionnels lors de la création d'une salle. [#17](https://github.com/tchapgouv/synapse-room-access-rules/issues/17)
- Correction : Il n'est plus possible de modifier le paramètre `visibility` après la création de la salle.
- Correction : Dans les salles publiques, le niveau d'autorisation pour l'invitation est maintenant défini par défaut à 0. [#18](https://github.com/tchapgouv/synapse-room-access-rules/issues/18)

### Évolutions techniques
- Refactoring : Renommage du paramètre `encrypted` en `force_unencrypted_at_creation` pour plus de clarté.
- Correction de problèmes de typage identifiés par mypy.
- Ajout d'un "fixer" pour ajouter la visibilité publique dans l'événement de règles d'accès pour les salles publiques.
- Amélioration du formatage du code.

### Autres changements
- Intégration de la branche `private-unencrypted-all`.
