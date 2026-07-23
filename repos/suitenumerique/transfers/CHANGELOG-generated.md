## Changelog : transfers (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la sécurité et à la fonctionnalité du service de transfert de fichiers. L'ajout du chiffrement de bout en bout optionnel et de l'analyse antivirus renforce la protection des données, tandis que des corrections améliorent la robustesse et la compatibilité du système.

### Évolutions fonctionnelles
- Ajout du chiffrement de bout en bout optionnel pour les transferts, offrant un contrôle accru sur la confidentialité des données [#14](https://github.com/suitenumerique/transfers/issues/14).
- Intégration d'un scanner de fichiers pour empêcher le stockage de fichiers dangereux [#9](https://github.com/suitenumerique/transfers/issues/9).

### Évolutions techniques
- Amélioration de la robustesse de l'analyse antivirus en cas de scanner indisponible.
- Correction des points soulevés lors de la revue du flux de re-scan.
- Autorisation de l'origine S3 dans la directive `connect-src` du CSP pour les uploads, corrigeant un problème de compatibilité.

### Autres changements
Aucun autre changement significatif à signaler.
