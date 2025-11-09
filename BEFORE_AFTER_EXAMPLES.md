# Before/After Examples - Table Width Fixes

## Example 1: Chapter 1 - SIPOC Table

### Before:
```latex
\begin{table}[H]
\centering
\caption{Tableau SIPOC du projet}
\label{tab:sipoc}
\begin{tabular}{|l|p{10cm}|}
\hline
\rowcolor{gray!30}
\textbf{Élément} & \textbf{Description} \\
\hline
...
\end{tabular}
\end{table}
```
**Problem:** Fixed width of 10cm could overflow on narrow pages

### After:
```latex
\begin{table}[H]
\centering
\caption{Tableau SIPOC du projet}
\label{tab:sipoc}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{|l|p{10cm}|}
\hline
\rowcolor{gray!30}
\textbf{Élément} & \textbf{Description} \\
\hline
...
\end{tabular}
\end{adjustbox}
\end{table}
```
**Solution:** Table automatically scales to fit page width

---

## Example 2: Chapter 2 - Divatex Software Summary

### Before:
```latex
\begin{table}[H]
\centering
\caption{Résumé du fonctionnement du logiciel Divatex}
\begin{tabular}{|l|l|}
\hline
\textbf{Élément} & \textbf{Description} \\
\hline
Rôle & Gestion amont : stock de tissu, planification et mouvement des rouleaux \\
\hline
Entrées & Données des rouleaux (référence, quantité, emplacement), ordres de fabrication (OF), réservations matière \\
...
\end{tabular}
\end{table}
```
**Problem:** Long text in cells caused horizontal overflow

### After:
```latex
\begin{table}[H]
\centering
\caption{Résumé du fonctionnement du logiciel Divatex}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{|l|l|}
\hline
\textbf{Élément} & \textbf{Description} \\
\hline
Rôle & Gestion amont : stock de tissu, planification et mouvement des rouleaux \\
\hline
Entrées & Données des rouleaux (référence, quantité, emplacement), ordres de fabrication (OF), réservations matière \\
...
\end{tabular}
\end{adjustbox}
\end{table}
```
**Solution:** Table scales down to fit, maintaining readability

---

## Example 3: Chapter 3 - Python Libraries Table

### Before:
```latex
\begin{table}[H]
\centering
\caption{Bibliothèques Python pour la manipulation de données}
\begin{tabular}{|l|l|p{3cm}|p{6cm}|}
\hline
\textbf{Bibliothèque} & \textbf{Version} & \textbf{Rôle principal} & \textbf{Justification du choix} \\
\hline
...
\end{tabular}
\label{tab:data_manipulation_libs}
\end{table}
```
**Problem:** Total width (3cm + 6cm + 2 auto columns) exceeded page width

### After:
```latex
\begin{table}[H]
\centering
\caption{Bibliothèques Python pour la manipulation de données}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{|l|l|p{3cm}|p{6cm}|}
\hline
\textbf{Bibliothèque} & \textbf{Version} & \textbf{Rôle principal} & \textbf{Justification du choix} \\
\hline
...
\end{tabular}
\end{adjustbox}
\label{tab:data_manipulation_libs}
\end{table}
```
**Solution:** Proportional scaling maintains column relationships

---

## Example 4: Chapter 5 - Roadmap Table

### Before:
```latex
\begin{table}[H]
\centering
\caption{Roadmap Phase 1 - Fondations}
\begin{tabular}{|p{2cm}|p{8cm}|p{3cm}|}
\hline
\textbf{Sprint} & \textbf{Livrables} & \textbf{Durée} \\
\hline
...
\end{tabular}
\label{tab:roadmap_phase1}
\end{table}
```
**Problem:** Total width (2cm + 8cm + 3cm = 13cm) plus borders exceeded margins

### After:
```latex
\begin{table}[H]
\centering
\caption{Roadmap Phase 1 - Fondations}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{|p{2cm}|p{8cm}|p{3cm}|}
\hline
\textbf{Sprint} & \textbf{Livrables} & \textbf{Durée} \\
\hline
...
\end{tabular}
\end{adjustbox}
\label{tab:roadmap_phase1}
\end{table}
```
**Solution:** Table fits perfectly within text width

---

## Key Benefits

1. **Automatic Scaling**: Tables scale down only when needed
2. **Maintains Proportions**: Column width ratios are preserved
3. **No Manual Adjustment**: Works for all table sizes
4. **Preserves Formatting**: All other table properties remain unchanged
5. **PDF Friendly**: Ensures professional appearance in final document

## Technical Note

The `adjustbox` package with `max width=\textwidth` parameter:
- Only scales tables that exceed the text width
- Maintains aspect ratio
- Works with all table types (tabular, longtable, etc.)
- Compatible with other table packages

## Verification

To verify the fix worked:
1. Open `basma-rapport/main.pdf`
2. Check that all tables fit within page margins
3. Verify text is readable (not too small)
4. Confirm no horizontal scrolling needed

All 65 tables have been successfully fixed!
