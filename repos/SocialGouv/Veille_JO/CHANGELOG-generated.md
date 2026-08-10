## Changelog : Veille_JO (30 derniers jours, au 07/08/2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'automatisation et de la distribution de l'outil. L'accent a été mis sur la facilité de consultation des archives, la précision de l'extraction des données de médicaments et la mise en place d'un système de publication automatique des rapports de veille.

### Évolutions fonctionnelles
- **Consultation des archives** : Amélioration de l'expérience utilisateur avec l'ajout de filtres, un affichage optimisé et un lien de retour à l'accueil sur les pages archivées.
- **Précision des données** : 
    - Meilleure gestion des nouvelles unités de mesure dans les noms de médicaments.
    - Correction du filtrage des mots-clés (suppression du terme "spécialité").
    - Correction du parsing des tableaux pour éviter l'inclusion erronée des titres.

### Évolutions techniques
- **Automatisation (CI/CD)** : 
    - Mise en place d'une GitHub Action pour la publication quotidienne automatique des rapports de veille sur GitHub Pages.
    - Ajout de la possibilité de spécifier une date manuellement lors du workflow de publication.
- **Distribution** : Automatisation de la génération de binaires autonomes (standalone) via Nuitka pour Windows, Linux et macOS, facilitant l'installation par les utilisateurs.

### Autres changements
- **Documentation** : 
    - Ajout d'instructions spécifiques pour l'installation sur macOS.
    - Réorganisation de la documentation de test (déplacement vers `TESTS.md`).
    - Mise à jour de la présentation du projet.
