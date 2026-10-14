## Changelog : docs (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois a été marqué par une transition majeure de l'architecture de collaboration vers le nouveau serveur YHub, apportant une plus grande robustesse et un support du mode hors-ligne. L'expérience utilisateur a été enrichie par de nouvelles capacités d'édition (duplication avec sous-documents, interliens automatiques) et un système de mentions plus performant. L'ensemble de l'infrastructure a également été renforcé pour permettre un meilleur monitoring et des tests de charge plus précis.

### Évolutions fonctionnelles
- **Édition et contenu** :
  - Ajout de la possibilité de télécharger les documents au format Markdown.
  - Introduction de la duplication de documents avec prise en charge des sous-documents.
  - Transformation automatique des liens de documents collés en interliens.
  - Amélioration de l'exportation PDF (maintien du ratio d'aspect des images et gestion des titres).
  - Support du défilement automatique vers un bloc lié en mode lecture seule.
- **Interactions et interface** :
  - Mise en place d'un système de mentions avec notifications par email (asynchrones et limitées par un délai de refroidissement).
  - Ajout de raccourcis clavier pour le mode présentation et indications visuelles des raccourcis dans les options.
  - Amélioration de la navigation : ouverture des résultats de recherche dans un nouvel onglet via Ctrl/Cmd+clic.
  - Redesign des pages d'erreur (401, 403 et 404) pour une meilleure expérience utilisateur.
  - Amélioration de l'accessibilité, notamment sur la structure de l'arbre documentaire [#2769](https://github.com/suitenumerique/docs/issues/2769).
- **Gestion des fichiers** :
  - Ajout d'un avertissement avant l'envoi de fichiers dépassant la taille limite autorisée.

### Évolutions techniques
- **Architecture de collaboration** :
  - Migration du serveur de collaboration de HocusPocus vers YHub, permettant notamment le support du mode hors-ligne.
  - Mise en place d'outils de migration pour transférer les anciens documents (S3) vers la nouvelle infrastructure.
  - Optimisation de la synchronisation et de la gestion des connexions lors de la suppression ou de la modification de documents.
- **Sécurité et Authentification** :
  - Publication de la clé publique JWT via un endpoint JWKS.
  - Renforcement de la sécurité des endpoints de collaboration et de la validation des tokens.
- **Observabilité et Performance** :
  - Intégration de métriques Prometheus et de tableaux de bord Grafana pour le suivi des performances et de la charge.
  - Ajout d'un outil de test de charge complet incluant des scénarios k6 et des "canaries" de navigateur pour mesurer l'expérience utilisateur sous charge.
- **Infrastructure et CI/CD** :
  - Optimisation des images Docker (passage à des versions "slim").
  - Amélioration des pipelines CI pour inclure les tests de charge et la vérification du serveur de collaboration.
  - Mise à jour des configurations Helm pour permettre une gestion plus fine des sondes (probes) et de l'indexation des moteurs de recherche.

### Autres changements
- **Documentation** :
  - Mise à jour complète de la documentation technique, incluant les guides d'installation, de migration vers YHub et de tests de charge.
  - Correction de plusieurs erreurs de typographie dans le README d'installation.
- **Internationalisation** :
  - Mise à jour importante des chaînes de caractères traduites et amélioration de la gestion du sélecteur de langue.
