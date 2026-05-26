## Changelog : synapse-room-access-rules (30 derniers jours, au 21 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des règles d'accès aux salles, notamment en introduisant la notion de visibilité (publique ou privée) et en permettant la création de salles privées non chiffrées. Des corrections ont également été apportées pour assurer la cohérence et la conformité du code.

### Évolutions fonctionnelles
- Ajout de la gestion de la visibilité des salles (publique ou privée) dans les règles d'accès. [#17](https://github.com/tchapgouv/synapse-room-access-rules/issues/17)
- Prise en charge des salles privées non chiffrées.
- Ajout d'un correcteur pour ajouter la visibilité publique par défaut aux événements de règles d'accès pour les salles publiques.
- Possibilité de forcer la création d'une salle non chiffrée même si le chiffrement est activé globalement.

### Évolutions techniques
- Renommage du paramètre `encrypted` en `force_unencrypted_at_creation` pour plus de clarté.
- Interdiction de modifier le paramètre `visibility` après la création d'une salle.
- Correction de problèmes de typage identifiés par mypy.
- Amélioration du formatage du code.

### Autres changements
- Aucune information supplémentaire à signaler.
