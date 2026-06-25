## Changelog : grist-utils (30 derniers jours, au 24 juin 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées aux utilitaires d'auto-hébergement de Grist. Les modifications incluent la mise à jour de la version de Node.js utilisée dans les tests CI, l'ajout de tests pour la validation de l'upload de fichiers multiples, et des mises à jour de dépendances pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Ajout de tests pour valider la possibilité d'uploader plusieurs fichiers dans une seule requête. [#1234](https://github.com/betagouv/grist-utils/issues/1234) (implémentation dans le commit `e619198`)

### Évolutions techniques
- Mise à jour de la version de Node.js à v24 dans les tests CI pour assurer la compatibilité et bénéficier des dernières améliorations. (commit `e9b0440`)
- Mise à jour des dépendances du projet, notamment `undici`, `js-yaml`, `form-data`, `esbuild`, `tsx` et `ws` dans le répertoire `/grist-deployment-tests`. Ces mises à jour visent à améliorer la sécurité et la stabilité.

### Autres changements
- Aucune information supplémentaire à signaler.
