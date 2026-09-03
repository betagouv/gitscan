## Changelog : anssi-recommandations-cyber (30 derniers jours, au 02/09/2026)

### Résumé
Cette période est marquée par une amélioration significative de la précision et de la fiabilité des réponses fournies par l'IA Albert. En enrichissant les données transmises au modèle avec des métadonnées plus précises (sections, codes de recommandation), le système garantit des citations plus fidèles et un classement des informations plus robuste.

### Évolutions fonctionnelles
- **Amélioration de la précision des citations** : L'IA utilise désormais des repères système (document, section, recommandation) pour identifier précisément les passages cités, ce qui fiabilise les sources sans dépendre uniquement de la qualité de l'OCR.

### Évolutions techniques
- **Enrichissement du contexte LLM** : Intégration de métadonnées détaillées (type de bloc, code de recommandation, chemin des sections) dans le contexte envoyé au modèle générateur pour améliorer la pertinence des réponses.
- **Optimisation du reclassement par l'IA** : Utilisation des métadonnées comme signaux prioritaires pour le processus de reclassement, tout en conservant l'analyse textuelle comme mécanisme de secours (fallback).
- **Mise à jour de la chaîne de données** : Propagation des nouvelles métadonnées de "chunks" depuis l'API Albert jusqu'au modèle `Paragraphe`, incluant une gestion de compatibilité pour les données indexées précédemment.

### Autres changements
- **Documentation** : Mise à jour du README et du descriptif du parcours d'interaction avec l'IA Albert.
