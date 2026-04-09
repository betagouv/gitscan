## Changelog : arretify (30 derniers jours, au 9 avril 2026)

### Résumé
Les dernières mises à jour d'Arrêtify se concentrent sur l'amélioration de la reconnaissance et de la structuration des arrêtés préfectoraux, notamment grâce à une meilleure intégration avec la version 3 de Mistral OCR.  De nombreuses corrections et optimisations ont été apportées pour gérer plus robustement les différents formats et les erreurs d'OCR, améliorant ainsi la qualité de la conversion en HTML sémantique.

### Évolutions fonctionnelles
- Amélioration de la détection du début du contenu principal des arrêtés.
- Support amélioré pour l'intégration de tableaux extraits par Mistral OCR, y compris les balises en ligne.
- Correction d'un bug concernant les balises de pagination dans les visas.
- Détection plus précise des titres de table des matières (TOC) et correction d'un bug lié au diviseur de TOC.
- Détection plus stricte des titres composés uniquement de chiffres.
- Amélioration de la détection et du traitement des en-têtes, avec application du nettoyage OCR.
- Correction de la détection des cadres (frames) qui étaient parfois identifiés à tort comme des tableaux avec Mistral OCR 3.
- Ajout du support pour les en-têtes et pieds de page extraits par Mistral 3.
- Intégration de l'inclusion d'images et du rendu dans le pré-traitement.

### Évolutions techniques
- Refonte du système de stockage des pages pour supporter Mistral 3.
- Introduction de la classe `Asset` pour gérer les ressources associées aux documents.
- Création d'un modèle `OcrDocument` pour encapsuler les pages d'un document OCRisé.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de docstrings pour les fonctions de séparation de texte.
- Ajout d'une option de repli si le mot-clé "arrêté" n'est pas trouvé.
- Restauration des snapshots à partir de la branche Mistral OCR3.
- Nettoyage et régénération des pages d'exemple avec Mistral OCR 3.

### Autres changements
- Régénération des snapshots de la page d'index.
- Correction de bugs et amélioration de la qualité de l'évaluation avec des ground truths mis à jour.
- Formatage du code avec `black`.
- Raccourcissement des chemins dans les jeux de données.
- Correction de titres dans les en-têtes.
- Correction de bugs liés à la description des tableaux OCR intégrés.
- Correction de l'enregistrement des documents OCR avec des fichiers non chargés.
- Mise à jour du markdown pour tester l'intégration des tableaux OCR.
- Correction de tests.
- Petites corrections diverses.
