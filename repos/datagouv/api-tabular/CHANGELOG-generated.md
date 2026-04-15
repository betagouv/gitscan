## Changelog : api-tabular (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration continue et le déploiement (CI/CD) avec la construction et la publication de l'image Docker directement depuis la chaîne CI d'Applicative. Une correction a également été apportée pour encapsuler correctement les noms de colonnes dans le paramètre `columns`, améliorant ainsi la robustesse de l'API.

### Évolutions fonctionnelles
- Correction : Les noms de colonnes sont maintenant correctement encapsulés pour le paramètre `columns`, évitant ainsi des erreurs potentielles lors de l'utilisation de noms de colonnes contenant des caractères spéciaux. [#107](https://github.com/datagouv/api-tabular/issues/107)

### Évolutions techniques
- CI/CD : L'image Docker est maintenant construite et poussée vers le registre depuis la chaîne CI d'Applicative. [#98](https://github.com/datagouv/api-tabular/issues/98)

### Autres changements
- Aucun changement significatif à signaler.
