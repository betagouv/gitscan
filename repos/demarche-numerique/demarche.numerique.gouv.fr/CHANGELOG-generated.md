## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 21 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives en matière de performance, de sécurité et d'expérience utilisateur. Des optimisations ont été apportées pour accélérer le traitement des dossiers, notamment pour les procédures déclaratives en attente. Plusieurs corrections de sécurité ont été implémentées pour prévenir des vulnérabilités potentielles, telles que des injections URL et des contournements de CSRF. L'interface utilisateur a également été améliorée, avec des corrections de bugs et des ajustements pour une meilleure accessibilité.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces jointes : ajout de la prise en charge du format KML [#12850](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12850).
- Amélioration de l'expérience utilisateur pour les avis externes : ajout d'un badge "Validé" sur les tuiles correspondantes [#12857](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12857).
- Possibilité pour les administrateurs de personnaliser la présentation par défaut des procédures pour les instructeurs [#12905](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12905).
- Ajout d'une notification aux administrateurs avant l'expiration du token API Entreprise [#12994](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12994).
- Amélioration de l'affichage des erreurs dans le formulaire d'importation [#12862](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12862).
- Ajout d'un lien vers la documentation dans le menu principal pour les utilisateurs, les instructeurs et les administrateurs [#12816](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12816).
- Correction d'un bug empêchant la soumission d'un dossier après la suppression d'une pièce jointe [#12856](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12856).

### Évolutions techniques
- **Performance:** Optimisations significatives pour accélérer la recherche et le traitement des dossiers en attente [#12998](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12998).
- **Sécurité:**
    - Correction de plusieurs vulnérabilités potentielles, notamment des injections URL, des contournements de CSRF et des failles XSS [#12995](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12995), [#12902](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12902), [#12832](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12832), [#12834](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12836), [#12838](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12838).
    - Renforcement de la validation des identifiants et des URLs pour prévenir les attaques potentielles.
    - Amélioration de la gestion des en-têtes HTTP pour renforcer la sécurité.
- **Infrastructure:** Mise à jour de plusieurs dépendances, notamment Rails et Bundler.
- **Refactoring:** Migration de composants HAML vers ERB pour une meilleure maintenabilité.
- **Tests:** Ajout de tests unitaires et système pour améliorer la couverture et la qualité du code.
- Utilisation de LightningCSS pour remplacer PostCSS/Autoprefixer [#12845](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12845).

### Autres changements
- Mise à jour de la documentation.
- Amélioration des messages d'erreur et de l'expérience utilisateur globale.
- Nettoyage du code et suppression de code obsolète.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Ajout d'une clé publique pour les packages Debian [#12854](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pulls/12854).
