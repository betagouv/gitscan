## Changelog : react-dsfr (30 derniers jours, au 19 août 2026)

### Résumé
Les récentes mises à jour améliorent l'accessibilité des alertes et optimisent les performances en permettant de ne charger que le CSS des composants réellement utilisés. Plusieurs corrections ont également été apportées pour stabiliser l'affichage des formulaires, des menus et des pieds de page.

### Évolutions fonctionnelles
- **Accessibilité** : Le composant `Alert` définit désormais automatiquement son rôle ARIA en fonction de son niveau de sévérité [#503](https://github.com/codegouvfr/react-dsfr/pull/503).
- **Corrections d'interface** :
  - Correction des classes CSS appliquées aux messages d'aide dans les champs de saisie (`Input`) [#492](https://github.com/codegouvfr/react-dsfr/pull/492).
  - Correction du type de données pour le nom des catégories dans le composant `Footer` [#493](https://github.com/codegouvfr/react-dsfr/pull/493).
  - Correction du type de bouton utilisé dans le menu latéral (`Side Menu`) [#501](https://github.com/codegouvfr/react-dsfr/pull/501).

### Évolutions techniques
- **Optimisation des performances** : Introduction d'une option permettant de ne conserver que le CSS des composants utilisés (`only-include-used-components`), réduisant ainsi le poids des fichiers pour l'utilisateur final [#505](https://github.com/codegouvfr/react-dsfr/pull/505).
- **CI/CD et Build** :
  - Correction du job de publication sur npm [#507](https://github.com/codegouvfr/react-dsfr/pull/507).
  - Ajustement du processus de build pour ignorer le fichier `index.html` lorsqu'il est absent [#506](https://github.com/codegouvfr/react-dsfr/pull/506).

### Autres changements
- Passage à la version 1.33.0.
