## Changelog : monitorfish (30 derniers jours, au 19/10/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience de cartographie, notamment avec le rétablissement de la navigation autour du globe. L'outil de gestion des signalements et des contrôles a été enrichi avec de nouvelles catégories d'infractions et une meilleure visibilité des champs obligatoires. Enfin, une mise en conformité avec le système de design de l'État (DSFR) a été entamée pour améliorer l'accessibilité et l'interface utilisateur.

### Évolutions fonctionnelles
- **Cartographie et SIG** :
    - Rétablissement de la navigation "tour du monde" (passage de l'antiméridien/Pacifique) [#5571].
    - Possibilité d'enregistrer l'organisation des couches cartographiques par profil utilisateur [#5501].
    - Ajout d'un sélecteur multi-zones dans les filtres de la carte.
    - Amélioration du rendu des étiquettes et des superpositions sur la vue globale.
- **Signalements et Contrôles** :
    - Ajout de nouveaux types de cibles (Engin) et de types de matériel (FAD) dans les formulaires de signalement [#5305].
    - Intégration de nouvelles catégories d'infractions (NATINF 33916 et 30033).
    - Amélioration de la gestion des contrôles : meilleure visibilité des champs manquants, ajout de tooltips et masquage automatique de certains champs selon l'engin utilisé [#5559].
    - Ajout de la possibilité de consulter les signalements archivés dans la vue liste [#5536].
- **Gestion des Navires et Missions** :
    - Ajout d'un filtre "Équipé VMS" dans la liste des navires [#5500].
    - Amélioration de la détection des dysfonctionnements de balises et affichage détaillé dans la fiche navire.
    - Optimisation des formulaires de missions : gestion plus fine des champs de maillage et mise en évidence des contrôles Oui/Non/NA.
- **Alertes et Monitoring** :
    - Mise en place de nouveaux flux d'alerte pour détecter les activités déclarées lors de dysfonctionnements de balises.
    - Ajout d'un bouton pour arrêter le suivi spécifique d'un dysfonctionnement de balise.
- **Interface et Accessibilité** :
    - Migration de la page de connexion vers le système de design de l'État (DSFR) [#5548].
    - Ajout d'une page de déclaration d'accessibilité accessible depuis la connexion [#5553].

### Évolutions techniques
- **Observabilité et Fiabilité** :
    - Amélioration du suivi des erreurs via Sentry, incluant la remontée des erreurs des flux (flows) via un proxy [#5538, #5539, #5541].
    - Implémentation de mécanismes de limitation de débit (rate limiting) et de tentatives automatiques (retries) sur l'API de profondeur pour éviter les erreurs de type "Too many requests" [#5487].
    - Résolution de problèmes de connexion aux bases de données Oracle [#5499].
    - Correction de nombreux tests automatisés (Cypress) pour réduire l'instabilité (flaky tests) [#5529].
- **Architecture et Backend** :
    - Remplacement du système de chat par un bot Tchap via webhook [#5514].
    - Refonte de la logique de gestion des dysfonctionnements de balises pour une meilleure précision.

### Autres changements
- **Documentation** : Mises à jour régulières de la documentation de l'application [#5527].
- **Open Data** : Mise à jour et upload de la réglementation sur la Géoplateforme [#5486].
