## Changelog : securix (30 derniers jours, au 2 juin 2026)

### Résumé
Cette version apporte des améliorations à la sécurité et à la stabilité de Securix. L'installateur est désormais plus robuste et idempotent, et la configuration est affinée pour une meilleure conformité aux recommandations ANSSI. Une option pour désactiver KWallet a également été ajoutée.

### Évolutions fonctionnelles
- Désactivation de KWallet pour renforcer la sécurité et la conformité. [#93](https://github.com/cloud-gouv/securix/pull/93)
- Amélioration de la robustesse de l'installateur : l'installation est désormais idempotente, ce qui signifie qu'elle peut être relancée sans provoquer d'effets indésirables. [#92](https://github.com/cloud-gouv/securix/pull/92)

### Évolutions techniques
- Correction dans la fonction `mkSysctlChecker` pour utiliser une comparaison de chaînes de caractères, améliorant ainsi la fiabilité des vérifications de configuration ANSSI. [#167](https://github.com/cloud-gouv/securix/issues/167)
- Ajout d'un test pour vérifier l'idempotence de l'installateur.

### Autres changements
- Mise à jour de la documentation (README) pour refléter les dernières évolutions. [#168](https://github.com/cloud-gouv/securix/pull/168)
