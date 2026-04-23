## Changelog : arretify (30 derniers jours, au 21 avril 2026)

### Résumé
Cette nouvelle version d'Arrêtify améliore significativement la conversion d'arrêtés préfectoraux en HTML. Les améliorations se concentrent sur la détection des titres, la gestion des tableaux issus de l'OCR, et la robustesse générale de l'analyse des documents. La version 0.2.0 est presque prête à être publiée.

### Évolutions fonctionnelles
- **Détection de titres améliorée :** Ajout d'abréviations pour les mots "article" afin d'améliorer la détection des titres. [#issue à investiguer]
- **Gestion des tableaux OCR :** Support ajouté pour les balises en ligne dans les tableaux extraits par OCR, permettant une meilleure restitution du formatage.
- **Détection de table des matières (TOC) :** Amélioration de la détection du titre de la table des matières et déplacement vers le corps de la page.
- **Robustesse accrue :** Ajout d'une option de repli si le mot-clé "arrêté" n'est pas trouvé, évitant ainsi des erreurs dans certains cas.
- **Détection du début du contenu principal :** Modification de la règle pour détecter le début du contenu principal du document.
- **Détection de titres numériques :** La détection des titres est désormais plus stricte pour les titres composés uniquement de chiffres.

### Évolutions techniques
- **Préparation de la version 0.2.0 :**  Préparation des derniers ajustements pour la publication de la version 0.2.0.
- **Correction de bugs :**
    - Correction d'un bug lié aux balises de pagination dans les visas.
    - Correction de la représentation des éléments d'en-tête.
    - Correction d'un bug dans le diviseur de table des matières.
- **Amélioration de la détection de page headers et footers** (via l'intégration de Mistral OCR 3, déjà mentionnée dans le CHANGELOG existant).
- **Traitement direct des tableaux en HTML** (via l'intégration de Mistral OCR 3, déjà mentionnée dans le CHANGELOG existant).

### Autres changements
- Correction d'une petite erreur de documentation.
