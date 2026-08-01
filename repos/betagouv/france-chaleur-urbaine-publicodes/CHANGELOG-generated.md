## Changelog : france-chaleur-urbaine-publicodes (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte une refonte majeure de la structure des règles métier du modèle Publicodes, en les organisant par mode de chauffage. Cette refactorisation vise à améliorer la lisibilité, la maintenabilité et l'extensibilité du code. Des mises à jour des données et des formules de calcul ont également été intégrées, notamment concernant les puissances souscrites, les coûts de l'électricité et le besoin en eau chaude sanitaire.

### Évolutions fonctionnelles
- Mise à jour de la puissance souscrite par défaut à 9 kVA.
- Augmentation du coût de l'abonnement à l'électricité de 4€.
- Modification de la formule de calcul du besoin en eau chaude sanitaire pour le résidentiel.
- Changement du mode de calcul pour les PAC air-eau individuelles (P4).
- Mise à jour du rendement des chaudières gaz.

### Évolutions techniques
- **Refactorisation majeure des règles métier :** Organisation des règles par mode de chauffage (gaz, fioul, granulés, etc.) pour une meilleure structure et lisibilité.  Les règles ont été déplacées dans `src/modes/` et `src/commun/`.
- **Simplification des règles :** Suppression de 99 règles obsolètes.
- **Amélioration de la documentation :** Documentation de l'architecture du modèle et de l'analyse critique de la refactorisation.
- **Golden master :** Ajout d'un harnais de tests "golden master" pour garantir la cohérence des calculs.
- **Formatage du code :** Utilisation de Biome pour le formatage du code.
- **Gestion des ratios :** Regroupement et organisation des ratios économiques et techniques.
- **Suppression de références internes :** Relativisation des références internes à chaque mode de chauffage.

### Autres changements
- Mise à jour de la version du projet à 2.0.0.
- Correction de bugs mineurs sans impact numérique.
- Ajout d'une commande `pack:local` pour faciliter le développement.
- Fix d'un problème avec TruffleHog dans le CI.
- Fusion des documents de documentation en un seul fichier `DOCUMENTATION.md`.
- Nettoyage du code et suppression de commentaires inutiles.
