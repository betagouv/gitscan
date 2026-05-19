## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la précision des données réglementaires, le suivi de l'utilisation via Matomo pour mieux comprendre le comportement des utilisateurs, et des corrections de bugs pour une meilleure expérience utilisateur. Des ajustements ont également été apportés à la recherche de parcelles et à la sécurité des emails.

### Évolutions fonctionnelles
- Amélioration de la recherche de parcelles : suppression de l'adresse dans l'URL après la recherche [#76](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/76).
- Précision des données réglementaires : modifications apportées au texte et à la vérification des catégories dans les réglementations [#72](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/72) et [#66](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/66).
- Correction de l'affichage des risques sonores dans le résumé du diagnostic.
- Amélioration de la gestion des sources de réglementation locale, suppression du PLU codé en dur [#69](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/69).
- Ajout de paramètres de requête spécifiques pour cibler les références de parcelles [#42e3ca4](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/42e3ca4).

### Évolutions techniques
- Intégration de Matomo pour le suivi du parcours utilisateur et la création de heatmaps [#75](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/75).
- Amélioration de l'isolation des fonctions de classification sonore avec des règles cumulatives [#09b3d69](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/09b3d69).
- Correction d'une erreur React lors du rendu [#7ba8034](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/7ba8034).
- Amélioration de la sécurité concernant la réception des emails de diagnostic [#99d23de](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/99d23de).
- Correction du type source vers sound_category dans RegulationCls [#37f1034](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/37f1034).

### Autres changements
- Mises à jour de version : passage de 0.1.0 à 0.1.1 puis à 0.1.2 [#73](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/73) et [#74](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/74).
- Ajout de tests pour les fonctions d'isolation [#f1aebe1](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/f1aebe1).
- Suppression de liens dans la description des réglementations [#12d81e9](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/12d81e9).
- Nettoyage et suppression de trackers Matomo inutiles [#84f83e2](https://github.com/betagouv/diagbruit.beta.gouv.fr/commit/84f83e2).
